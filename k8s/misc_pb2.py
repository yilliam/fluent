# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: misc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='misc.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nmisc.proto\"-\n\tDataValue\x12\r\n\x05value\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x03\"o\n\x16ServerThreadStatistics\x12\x1b\n\x13storage_consumption\x18\x01 \x02(\x04\x12\x11\n\toccupancy\x18\x02 \x02(\x01\x12\r\n\x05\x65poch\x18\x03 \x02(\r\x12\x16\n\x0etotal_accesses\x18\x04 \x02(\r\"e\n\rKeyAccessData\x12%\n\x04keys\x18\x01 \x03(\x0b\x32\x17.KeyAccessData.KeyCount\x1a-\n\x08KeyCount\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_count\x18\x02 \x02(\r\"\xc1\x01\n\x0eTierMembership\x12\x12\n\nstart_time\x18\x01 \x02(\x04\x12#\n\x05tiers\x18\x02 \x03(\x0b\x32\x14.TierMembership.Tier\x1av\n\x04Tier\x12\x0f\n\x07tier_id\x18\x01 \x02(\r\x12,\n\x07servers\x18\x02 \x03(\x0b\x32\x1b.TierMembership.Tier.Server\x1a/\n\x06Server\x12\x11\n\tpublic_ip\x18\x01 \x02(\t\x12\x12\n\nprivate_ip\x18\x02 \x02(\t\"\xbb\x01\n\x0cUserFeedback\x12\x0b\n\x03uid\x18\x01 \x02(\t\x12\x0f\n\x07latency\x18\x02 \x01(\x01\x12\x0e\n\x06\x66inish\x18\x03 \x01(\x08\x12\x12\n\nthroughput\x18\x04 \x01(\x01\x12\x0e\n\x06warmup\x18\x05 \x01(\x08\x12-\n\x0bkey_latency\x18\x06 \x03(\x0b\x32\x18.UserFeedback.KeyLatency\x1a*\n\nKeyLatency\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x0f\n\x07latency\x18\x02 \x02(\x01\"\\\n\x0bKeySizeData\x12\'\n\tkey_sizes\x18\x01 \x03(\x0b\x32\x14.KeySizeData.KeySize\x1a$\n\x07KeySize\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x0c\n\x04size\x18\x02 \x02(\r')
)




_DATAVALUE = _descriptor.Descriptor(
  name='DataValue',
  full_name='DataValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='DataValue.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='DataValue.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=59,
)


_SERVERTHREADSTATISTICS = _descriptor.Descriptor(
  name='ServerThreadStatistics',
  full_name='ServerThreadStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storage_consumption', full_name='ServerThreadStatistics.storage_consumption', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupancy', full_name='ServerThreadStatistics.occupancy', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='ServerThreadStatistics.epoch', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_accesses', full_name='ServerThreadStatistics.total_accesses', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=172,
)


_KEYACCESSDATA_KEYCOUNT = _descriptor.Descriptor(
  name='KeyCount',
  full_name='KeyAccessData.KeyCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='KeyAccessData.KeyCount.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_count', full_name='KeyAccessData.KeyCount.access_count', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=275,
)

_KEYACCESSDATA = _descriptor.Descriptor(
  name='KeyAccessData',
  full_name='KeyAccessData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='KeyAccessData.keys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_KEYACCESSDATA_KEYCOUNT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=275,
)


_TIERMEMBERSHIP_TIER_SERVER = _descriptor.Descriptor(
  name='Server',
  full_name='TierMembership.Tier.Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_ip', full_name='TierMembership.Tier.Server.public_ip', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_ip', full_name='TierMembership.Tier.Server.private_ip', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=471,
)

_TIERMEMBERSHIP_TIER = _descriptor.Descriptor(
  name='Tier',
  full_name='TierMembership.Tier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tier_id', full_name='TierMembership.Tier.tier_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='servers', full_name='TierMembership.Tier.servers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TIERMEMBERSHIP_TIER_SERVER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=471,
)

_TIERMEMBERSHIP = _descriptor.Descriptor(
  name='TierMembership',
  full_name='TierMembership',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='TierMembership.start_time', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tiers', full_name='TierMembership.tiers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TIERMEMBERSHIP_TIER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=471,
)


_USERFEEDBACK_KEYLATENCY = _descriptor.Descriptor(
  name='KeyLatency',
  full_name='UserFeedback.KeyLatency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='UserFeedback.KeyLatency.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latency', full_name='UserFeedback.KeyLatency.latency', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=661,
)

_USERFEEDBACK = _descriptor.Descriptor(
  name='UserFeedback',
  full_name='UserFeedback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='UserFeedback.uid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latency', full_name='UserFeedback.latency', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish', full_name='UserFeedback.finish', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throughput', full_name='UserFeedback.throughput', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warmup', full_name='UserFeedback.warmup', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_latency', full_name='UserFeedback.key_latency', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_USERFEEDBACK_KEYLATENCY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=661,
)


_KEYSIZEDATA_KEYSIZE = _descriptor.Descriptor(
  name='KeySize',
  full_name='KeySizeData.KeySize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='KeySizeData.KeySize.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='KeySizeData.KeySize.size', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=719,
  serialized_end=755,
)

_KEYSIZEDATA = _descriptor.Descriptor(
  name='KeySizeData',
  full_name='KeySizeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_sizes', full_name='KeySizeData.key_sizes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_KEYSIZEDATA_KEYSIZE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=755,
)

_KEYACCESSDATA_KEYCOUNT.containing_type = _KEYACCESSDATA
_KEYACCESSDATA.fields_by_name['keys'].message_type = _KEYACCESSDATA_KEYCOUNT
_TIERMEMBERSHIP_TIER_SERVER.containing_type = _TIERMEMBERSHIP_TIER
_TIERMEMBERSHIP_TIER.fields_by_name['servers'].message_type = _TIERMEMBERSHIP_TIER_SERVER
_TIERMEMBERSHIP_TIER.containing_type = _TIERMEMBERSHIP
_TIERMEMBERSHIP.fields_by_name['tiers'].message_type = _TIERMEMBERSHIP_TIER
_USERFEEDBACK_KEYLATENCY.containing_type = _USERFEEDBACK
_USERFEEDBACK.fields_by_name['key_latency'].message_type = _USERFEEDBACK_KEYLATENCY
_KEYSIZEDATA_KEYSIZE.containing_type = _KEYSIZEDATA
_KEYSIZEDATA.fields_by_name['key_sizes'].message_type = _KEYSIZEDATA_KEYSIZE
DESCRIPTOR.message_types_by_name['DataValue'] = _DATAVALUE
DESCRIPTOR.message_types_by_name['ServerThreadStatistics'] = _SERVERTHREADSTATISTICS
DESCRIPTOR.message_types_by_name['KeyAccessData'] = _KEYACCESSDATA
DESCRIPTOR.message_types_by_name['TierMembership'] = _TIERMEMBERSHIP
DESCRIPTOR.message_types_by_name['UserFeedback'] = _USERFEEDBACK
DESCRIPTOR.message_types_by_name['KeySizeData'] = _KEYSIZEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataValue = _reflection.GeneratedProtocolMessageType('DataValue', (_message.Message,), dict(
  DESCRIPTOR = _DATAVALUE,
  __module__ = 'misc_pb2'
  # @@protoc_insertion_point(class_scope:DataValue)
  ))
_sym_db.RegisterMessage(DataValue)

ServerThreadStatistics = _reflection.GeneratedProtocolMessageType('ServerThreadStatistics', (_message.Message,), dict(
  DESCRIPTOR = _SERVERTHREADSTATISTICS,
  __module__ = 'misc_pb2'
  # @@protoc_insertion_point(class_scope:ServerThreadStatistics)
  ))
_sym_db.RegisterMessage(ServerThreadStatistics)

KeyAccessData = _reflection.GeneratedProtocolMessageType('KeyAccessData', (_message.Message,), dict(

  KeyCount = _reflection.GeneratedProtocolMessageType('KeyCount', (_message.Message,), dict(
    DESCRIPTOR = _KEYACCESSDATA_KEYCOUNT,
    __module__ = 'misc_pb2'
    # @@protoc_insertion_point(class_scope:KeyAccessData.KeyCount)
    ))
  ,
  DESCRIPTOR = _KEYACCESSDATA,
  __module__ = 'misc_pb2'
  # @@protoc_insertion_point(class_scope:KeyAccessData)
  ))
_sym_db.RegisterMessage(KeyAccessData)
_sym_db.RegisterMessage(KeyAccessData.KeyCount)

TierMembership = _reflection.GeneratedProtocolMessageType('TierMembership', (_message.Message,), dict(

  Tier = _reflection.GeneratedProtocolMessageType('Tier', (_message.Message,), dict(

    Server = _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), dict(
      DESCRIPTOR = _TIERMEMBERSHIP_TIER_SERVER,
      __module__ = 'misc_pb2'
      # @@protoc_insertion_point(class_scope:TierMembership.Tier.Server)
      ))
    ,
    DESCRIPTOR = _TIERMEMBERSHIP_TIER,
    __module__ = 'misc_pb2'
    # @@protoc_insertion_point(class_scope:TierMembership.Tier)
    ))
  ,
  DESCRIPTOR = _TIERMEMBERSHIP,
  __module__ = 'misc_pb2'
  # @@protoc_insertion_point(class_scope:TierMembership)
  ))
_sym_db.RegisterMessage(TierMembership)
_sym_db.RegisterMessage(TierMembership.Tier)
_sym_db.RegisterMessage(TierMembership.Tier.Server)

UserFeedback = _reflection.GeneratedProtocolMessageType('UserFeedback', (_message.Message,), dict(

  KeyLatency = _reflection.GeneratedProtocolMessageType('KeyLatency', (_message.Message,), dict(
    DESCRIPTOR = _USERFEEDBACK_KEYLATENCY,
    __module__ = 'misc_pb2'
    # @@protoc_insertion_point(class_scope:UserFeedback.KeyLatency)
    ))
  ,
  DESCRIPTOR = _USERFEEDBACK,
  __module__ = 'misc_pb2'
  # @@protoc_insertion_point(class_scope:UserFeedback)
  ))
_sym_db.RegisterMessage(UserFeedback)
_sym_db.RegisterMessage(UserFeedback.KeyLatency)

KeySizeData = _reflection.GeneratedProtocolMessageType('KeySizeData', (_message.Message,), dict(

  KeySize = _reflection.GeneratedProtocolMessageType('KeySize', (_message.Message,), dict(
    DESCRIPTOR = _KEYSIZEDATA_KEYSIZE,
    __module__ = 'misc_pb2'
    # @@protoc_insertion_point(class_scope:KeySizeData.KeySize)
    ))
  ,
  DESCRIPTOR = _KEYSIZEDATA,
  __module__ = 'misc_pb2'
  # @@protoc_insertion_point(class_scope:KeySizeData)
  ))
_sym_db.RegisterMessage(KeySizeData)
_sym_db.RegisterMessage(KeySizeData.KeySize)


# @@protoc_insertion_point(module_scope)