#  Copyright 2018 U.C. Berkeley RISE Lab
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging
import random
import sys
import time
import uuid
import zmq

from anna.client import AnnaClient
from anna.zmq_util import SocketCache
from include.kvs_pb2 import *
from include.functions_pb2 import *
from include import server_utils as sutils
from include.shared import *
from include.serializer import *
from .create import *
from .call import *
from . import utils

THRESHOLD = 10 # how often metadata is updated

def scheduler(ip, mgmt_ip, route_addr):
    logging.basicConfig(filename='log_scheduler.txt', level=logging.INFO)

    kvs = AnnaClient(route_addr, ip)

    key_cache_map = {}
    key_ip_map = {}
    ctx = zmq.Context(1)

    # Each dag consists of a set of functions and connections. Each one of
    # the functions is pinned to one or more nodes, which is tracked here.
    dags = {}
    thread_statuses = {}
    func_locations = {}

    connect_socket = ctx.socket(zmq.REP)
    connect_socket.bind(sutils.BIND_ADDR_TEMPLATE % (CONNECT_PORT))

    func_create_socket = ctx.socket(zmq.REP)
    func_create_socket.bind(sutils.BIND_ADDR_TEMPLATE % (FUNC_CREATE_PORT))

    func_call_socket = ctx.socket(zmq.REP)
    func_call_socket.bind(sutils.BIND_ADDR_TEMPLATE % (FUNC_CALL_PORT))

    dag_create_socket = ctx.socket(zmq.REP)
    dag_create_socket.bind(sutils.BIND_ADDR_TEMPLATE % (DAG_CREATE_PORT))

    dag_call_socket = ctx.socket(zmq.REP)
    dag_call_socket.bind(sutils.BIND_ADDR_TEMPLATE % (DAG_CALL_PORT))

    list_socket = ctx.socket(zmq.REP)
    list_socket.bind(sutils.BIND_ADDR_TEMPLATE % (LIST_PORT))

    exec_status_socket = ctx.socket(zmq.PULL)
    exec_status_socket.bind(sutils.BIND_ADDR_TEMPLATE % (sutils.STATUS_PORT))

    sched_update_socket = ctx.socket(zmq.PULL)
    sched_update_socket.bind(sutils.BIND_ADDR_TEMPLATE % (sutils.SCHED_UPDATE_PORT))

    requestor_cache = SocketCache(ctx, zmq.REQ)
    pusher_cache = SocketCache(ctx, zmq.PUSH)

    poller = zmq.Poller()
    poller.register(connect_socket, zmq.POLLIN)
    poller.register(func_create_socket, zmq.POLLIN)
    poller.register(func_call_socket, zmq.POLLIN)
    poller.register(dag_create_socket, zmq.POLLIN)
    poller.register(dag_call_socket, zmq.POLLIN)
    poller.register(list_socket, zmq.POLLIN)
    poller.register(exec_status_socket, zmq.POLLIN)
    poller.register(sched_update_socket, zmq.POLLIN)

    departed_executors = set()
    executors, schedulers = _update_cluster_state(requestor_cache, mgmt_ip,
            departed_executors, key_cache_map, key_ip_map, kvs)

    # track how often each DAG function is called
    call_frequency = {}


    start = time.time()

    while True:
        socks = dict(poller.poll(timeout=1000))

        if connect_socket in socks and socks[connect_socket] == zmq.POLLIN:
            msg = connect_socket.recv_string()
            connect_socket.send_string(routing_addr)

        if func_create_socket in socks and socks[func_create_socket] == zmq.POLLIN:
            create_func(func_create_socket, kvs)

        if func_call_socket in socks and socks[func_call_socket] == zmq.POLLIN:
            call_function(func_call_socket, requestor_cache, executors, key_ip_map)

        if dag_create_socket in socks and socks[dag_create_socket] == zmq.POLLIN:
            create_dag(dag_create_socket, requestor_cache, kvs, executors,
                    dags, func_locations, call_frequency)

        if dag_call_socket in socks and socks[dag_call_socket] == zmq.POLLIN:
            call = DagCall()
            call.ParseFromString(dag_call_socket.recv())
            exec_id = generate_timestamp(0)

            dag = dags[call.name]
            for fname in dag[0].functions:
                call_frequency[fname] += 1

            accepted, error, rid = call_dag(call, requestor_cache,
                    pusher_cache, dags, func_locations, key_ip_map)

            while not accepted:
                # the assumption here is that the request was not accepted
                # because the cluster was out of date -- so we update cluster
                # state before proceeding
                executors, schedulers = _update_cluster_state(requestor_cache,
                        mgmt_ip, departed_executors, key_cache_map, key_ip_map,
                        kvs)

                accepted, error, rid = call_dag(call, requestor_cache,
                        pusher_cache, dags, func_locations, key_ip_map)

            resp = GenericResponse()
            resp.success = True
            resp.response_id = rid
            dag_call_socket.send(resp.SerializeToString())

        if list_socket in socks and socks[list_socket] == zmq.POLLIN:
            logging.info('Received query for function list.')
            msg = list_socket.recv_string()
            prefix = msg if msg else ''

            resp = FunctionList()
            resp.names.append(_get_func_list(client, prefix))

            list_socket.send(resp.SerializeToString())

        if exec_status_socket in socks and socks[exec_status_socket] == \
                zmq.POLLIN:
            status = ThreadStatus()
            status.ParseFromString(exec_status_socket.recv())

            key = (status.ip, status.tid)
            logging.info('Received status update from executor %s:%d.' %
                    (key[0], int(key[1])))

            # this means that this node is currently departing, so we remove it
            # from all of our metadata tracking
            if not status.running:
                old_status = thread_statuses[key]

                executors.remove(key)
                departed_executors.add(status.ip)
                del thread_statuses[key]

                for fname in old_status.functions:
                    func_locations[fname].remove(old_status.ip, old_status.tid)

                continue

            if key not in thread_statuses:
                thread_statuses[key] = status

                if key not in executors:
                    executors.add(key)
            elif thread_statuses[key] != status:
                # remove all the old function locations, and all the new ones
                # -- there will probably be a large overlap, but this shouldn't
                # be much different than calculating two different set
                # differences anyway
                for func in thread_statuses[key].functions:
                    if func in func_locations:
                        func_locations[func].discard(key)

                for func in status.functions:
                    if func not in func_locations:
                        func_locations[func] = set()

                    func_locations[func].add(key)

                thread_statuses[key] = status

        if sched_update_socket in socks and socks[sched_update_socket] == \
                zmq.POLLIN:
            logging.info('Received update from another scheduler.')
            ks = KeySet()
            ks.ParseFromString(sched_update_socket.recv())

            # retrieve any DAG that some other scheduler knows about that we do
            # not yet know about
            for dname in ks.keys:
                if dname not in dags:
                    dag = Dag()
                    dag.ParseFromString(kvs.get(dname).value)

                    dags[dname] = dag

        end = time.time()
        if end - start > THRESHOLD:
            executors, schedulers = _update_cluster_state(requestor_cache,
                    mgmt_ip, departed_executors, key_cache_map, key_ip_map, kvs)

            dag_names = KeySet()
            for name in dags.keys():
                dag_names.keys.append(name)
            msg = dag_names.SerializeToString()

            for sched_ip in schedulers:
                if sched_ip != ip:
                    pusher_cache.get(utils._get_scheduler_update_address(sched_ip))
                    sckt.send(msg)

            stats = ExecutorStatistics()
            for fname in call_frequency:
                fstats = stats.statistics.add()
                fstats.fname = fname
                fstats.call_count = call_frequency[fname]

                call_frequency[fname] = 0

            sckt = pusher_cache.get(sutils._get_statistics_report_address \
                    (mgmt_ip))
            sckt.send(stats.SerializeToString())

            start = time.time()

def _update_cluster_state(requestor_cache, mgmt_ip, departed_executors,
        key_cache_map, key_ip_map, kvs):
    # update our local key-cache mapping information
    executors = utils._get_ip_set(utils._get_executor_list_address(mgmt_ip),
            requestor_cache, True)

    # remove any function executor nodes that might still be running
    # but that we know are departed
    for departed in departed_executors:
        executors.remove(departed)

    utils._update_key_maps(key_cache_map, key_ip_map, executors, kvs)

    schedulers = utils._get_ip_set(utils._get_scheduler_list_address(mgmt_ip),
            requestor_cache, False)

    return executors, schedulers
