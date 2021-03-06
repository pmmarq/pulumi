# Copyright 2016-2018, Pulumi Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: provider.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import plugin_pb2 as plugin__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='provider.proto',
  package='pulumirpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0eprovider.proto\x12\tpulumirpc\x1a\x0cplugin.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x83\x01\n\x10\x43onfigureRequest\x12=\n\tvariables\x18\x01 \x03(\x0b\x32*.pulumirpc.ConfigureRequest.VariablesEntry\x1a\x30\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x01\n\x19\x43onfigureErrorMissingKeys\x12\x44\n\x0bmissingKeys\x18\x01 \x03(\x0b\x32/.pulumirpc.ConfigureErrorMissingKeys.MissingKey\x1a/\n\nMissingKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"C\n\rInvokeRequest\x12\x0b\n\x03tok\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"d\n\x0eInvokeResponse\x12\'\n\x06return\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\"i\n\x0c\x43heckRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12%\n\x04olds\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"c\n\rCheckResponse\x12\'\n\x06inputs\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\"0\n\x0c\x43heckFailure\x12\x10\n\x08property\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"t\n\x0b\x44iffRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12%\n\x04olds\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xc3\x01\n\x0c\x44iffResponse\x12\x10\n\x08replaces\x18\x01 \x03(\t\x12\x0f\n\x07stables\x18\x02 \x03(\t\x12\x1b\n\x13\x64\x65leteBeforeReplace\x18\x03 \x01(\x08\x12\x34\n\x07\x63hanges\x18\x04 \x01(\x0e\x32#.pulumirpc.DiffResponse.DiffChanges\"=\n\x0b\x44iffChanges\x12\x10\n\x0c\x44IFF_UNKNOWN\x10\x00\x12\r\n\tDIFF_NONE\x10\x01\x12\r\n\tDIFF_SOME\x10\x02\"I\n\rCreateRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"I\n\x0e\x43reateResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"S\n\x0bReadRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"G\n\x0cReadResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"v\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12%\n\x04olds\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"=\n\x0eUpdateResponse\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"U\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct2\xcd\x04\n\x10ResourceProvider\x12\x42\n\tConfigure\x12\x1b.pulumirpc.ConfigureRequest\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\x06Invoke\x12\x18.pulumirpc.InvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x12<\n\x05\x43heck\x12\x17.pulumirpc.CheckRequest\x1a\x18.pulumirpc.CheckResponse\"\x00\x12\x39\n\x04\x44iff\x12\x16.pulumirpc.DiffRequest\x1a\x17.pulumirpc.DiffResponse\"\x00\x12?\n\x06\x43reate\x12\x18.pulumirpc.CreateRequest\x1a\x19.pulumirpc.CreateResponse\"\x00\x12\x39\n\x04Read\x12\x16.pulumirpc.ReadRequest\x1a\x17.pulumirpc.ReadResponse\"\x00\x12?\n\x06Update\x12\x18.pulumirpc.UpdateRequest\x1a\x19.pulumirpc.UpdateResponse\"\x00\x12<\n\x06\x44\x65lete\x12\x18.pulumirpc.DeleteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12@\n\rGetPluginInfo\x12\x16.google.protobuf.Empty\x1a\x15.pulumirpc.PluginInfo\"\x00\x62\x06proto3')
  ,
  dependencies=[plugin__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_DIFFRESPONSE_DIFFCHANGES = _descriptor.EnumDescriptor(
  name='DiffChanges',
  full_name='pulumirpc.DiffResponse.DiffChanges',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIFF_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIFF_NONE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIFF_SOME', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1067,
  serialized_end=1128,
)
_sym_db.RegisterEnumDescriptor(_DIFFRESPONSE_DIFFCHANGES)


_CONFIGUREREQUEST_VARIABLESENTRY = _descriptor.Descriptor(
  name='VariablesEntry',
  full_name='pulumirpc.ConfigureRequest.VariablesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pulumirpc.ConfigureRequest.VariablesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pulumirpc.ConfigureRequest.VariablesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=234,
)

_CONFIGUREREQUEST = _descriptor.Descriptor(
  name='ConfigureRequest',
  full_name='pulumirpc.ConfigureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variables', full_name='pulumirpc.ConfigureRequest.variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGUREREQUEST_VARIABLESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=234,
)


_CONFIGUREERRORMISSINGKEYS_MISSINGKEY = _descriptor.Descriptor(
  name='MissingKey',
  full_name='pulumirpc.ConfigureErrorMissingKeys.MissingKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.ConfigureErrorMissingKeys.MissingKey.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pulumirpc.ConfigureErrorMissingKeys.MissingKey.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=383,
)

_CONFIGUREERRORMISSINGKEYS = _descriptor.Descriptor(
  name='ConfigureErrorMissingKeys',
  full_name='pulumirpc.ConfigureErrorMissingKeys',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='missingKeys', full_name='pulumirpc.ConfigureErrorMissingKeys.missingKeys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGUREERRORMISSINGKEYS_MISSINGKEY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=383,
)


_INVOKEREQUEST = _descriptor.Descriptor(
  name='InvokeRequest',
  full_name='pulumirpc.InvokeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tok', full_name='pulumirpc.InvokeRequest.tok', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='pulumirpc.InvokeRequest.args', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=452,
)


_INVOKERESPONSE = _descriptor.Descriptor(
  name='InvokeResponse',
  full_name='pulumirpc.InvokeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return', full_name='pulumirpc.InvokeResponse.return', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failures', full_name='pulumirpc.InvokeResponse.failures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=554,
)


_CHECKREQUEST = _descriptor.Descriptor(
  name='CheckRequest',
  full_name='pulumirpc.CheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.CheckRequest.urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='olds', full_name='pulumirpc.CheckRequest.olds', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='news', full_name='pulumirpc.CheckRequest.news', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=661,
)


_CHECKRESPONSE = _descriptor.Descriptor(
  name='CheckResponse',
  full_name='pulumirpc.CheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='pulumirpc.CheckResponse.inputs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failures', full_name='pulumirpc.CheckResponse.failures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=762,
)


_CHECKFAILURE = _descriptor.Descriptor(
  name='CheckFailure',
  full_name='pulumirpc.CheckFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='property', full_name='pulumirpc.CheckFailure.property', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='pulumirpc.CheckFailure.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=812,
)


_DIFFREQUEST = _descriptor.Descriptor(
  name='DiffRequest',
  full_name='pulumirpc.DiffRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.DiffRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.DiffRequest.urn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='olds', full_name='pulumirpc.DiffRequest.olds', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='news', full_name='pulumirpc.DiffRequest.news', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=814,
  serialized_end=930,
)


_DIFFRESPONSE = _descriptor.Descriptor(
  name='DiffResponse',
  full_name='pulumirpc.DiffResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replaces', full_name='pulumirpc.DiffResponse.replaces', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stables', full_name='pulumirpc.DiffResponse.stables', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteBeforeReplace', full_name='pulumirpc.DiffResponse.deleteBeforeReplace', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changes', full_name='pulumirpc.DiffResponse.changes', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DIFFRESPONSE_DIFFCHANGES,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=933,
  serialized_end=1128,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='pulumirpc.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.CreateRequest.urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.CreateRequest.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1130,
  serialized_end=1203,
)


_CREATERESPONSE = _descriptor.Descriptor(
  name='CreateResponse',
  full_name='pulumirpc.CreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.CreateResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.CreateResponse.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1205,
  serialized_end=1278,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='pulumirpc.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.ReadRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.ReadRequest.urn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.ReadRequest.properties', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1280,
  serialized_end=1363,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='pulumirpc.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.ReadResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.ReadResponse.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1365,
  serialized_end=1436,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='pulumirpc.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.UpdateRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.UpdateRequest.urn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='olds', full_name='pulumirpc.UpdateRequest.olds', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='news', full_name='pulumirpc.UpdateRequest.news', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1438,
  serialized_end=1556,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='pulumirpc.UpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.UpdateResponse.properties', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1558,
  serialized_end=1619,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='pulumirpc.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.DeleteRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.DeleteRequest.urn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.DeleteRequest.properties', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1621,
  serialized_end=1706,
)

_CONFIGUREREQUEST_VARIABLESENTRY.containing_type = _CONFIGUREREQUEST
_CONFIGUREREQUEST.fields_by_name['variables'].message_type = _CONFIGUREREQUEST_VARIABLESENTRY
_CONFIGUREERRORMISSINGKEYS_MISSINGKEY.containing_type = _CONFIGUREERRORMISSINGKEYS
_CONFIGUREERRORMISSINGKEYS.fields_by_name['missingKeys'].message_type = _CONFIGUREERRORMISSINGKEYS_MISSINGKEY
_INVOKEREQUEST.fields_by_name['args'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INVOKERESPONSE.fields_by_name['return'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INVOKERESPONSE.fields_by_name['failures'].message_type = _CHECKFAILURE
_CHECKREQUEST.fields_by_name['olds'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CHECKREQUEST.fields_by_name['news'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CHECKRESPONSE.fields_by_name['inputs'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CHECKRESPONSE.fields_by_name['failures'].message_type = _CHECKFAILURE
_DIFFREQUEST.fields_by_name['olds'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DIFFREQUEST.fields_by_name['news'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DIFFRESPONSE.fields_by_name['changes'].enum_type = _DIFFRESPONSE_DIFFCHANGES
_DIFFRESPONSE_DIFFCHANGES.containing_type = _DIFFRESPONSE
_CREATEREQUEST.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CREATERESPONSE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_READREQUEST.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_READRESPONSE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATEREQUEST.fields_by_name['olds'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATEREQUEST.fields_by_name['news'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATERESPONSE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DELETEREQUEST.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['ConfigureRequest'] = _CONFIGUREREQUEST
DESCRIPTOR.message_types_by_name['ConfigureErrorMissingKeys'] = _CONFIGUREERRORMISSINGKEYS
DESCRIPTOR.message_types_by_name['InvokeRequest'] = _INVOKEREQUEST
DESCRIPTOR.message_types_by_name['InvokeResponse'] = _INVOKERESPONSE
DESCRIPTOR.message_types_by_name['CheckRequest'] = _CHECKREQUEST
DESCRIPTOR.message_types_by_name['CheckResponse'] = _CHECKRESPONSE
DESCRIPTOR.message_types_by_name['CheckFailure'] = _CHECKFAILURE
DESCRIPTOR.message_types_by_name['DiffRequest'] = _DIFFREQUEST
DESCRIPTOR.message_types_by_name['DiffResponse'] = _DIFFRESPONSE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigureRequest = _reflection.GeneratedProtocolMessageType('ConfigureRequest', (_message.Message,), dict(

  VariablesEntry = _reflection.GeneratedProtocolMessageType('VariablesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGUREREQUEST_VARIABLESENTRY,
    __module__ = 'provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureRequest.VariablesEntry)
    ))
  ,
  DESCRIPTOR = _CONFIGUREREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureRequest)
  ))
_sym_db.RegisterMessage(ConfigureRequest)
_sym_db.RegisterMessage(ConfigureRequest.VariablesEntry)

ConfigureErrorMissingKeys = _reflection.GeneratedProtocolMessageType('ConfigureErrorMissingKeys', (_message.Message,), dict(

  MissingKey = _reflection.GeneratedProtocolMessageType('MissingKey', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGUREERRORMISSINGKEYS_MISSINGKEY,
    __module__ = 'provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureErrorMissingKeys.MissingKey)
    ))
  ,
  DESCRIPTOR = _CONFIGUREERRORMISSINGKEYS,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureErrorMissingKeys)
  ))
_sym_db.RegisterMessage(ConfigureErrorMissingKeys)
_sym_db.RegisterMessage(ConfigureErrorMissingKeys.MissingKey)

InvokeRequest = _reflection.GeneratedProtocolMessageType('InvokeRequest', (_message.Message,), dict(
  DESCRIPTOR = _INVOKEREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.InvokeRequest)
  ))
_sym_db.RegisterMessage(InvokeRequest)

InvokeResponse = _reflection.GeneratedProtocolMessageType('InvokeResponse', (_message.Message,), dict(
  DESCRIPTOR = _INVOKERESPONSE,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.InvokeResponse)
  ))
_sym_db.RegisterMessage(InvokeResponse)

CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CheckRequest)
  ))
_sym_db.RegisterMessage(CheckRequest)

CheckResponse = _reflection.GeneratedProtocolMessageType('CheckResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKRESPONSE,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CheckResponse)
  ))
_sym_db.RegisterMessage(CheckResponse)

CheckFailure = _reflection.GeneratedProtocolMessageType('CheckFailure', (_message.Message,), dict(
  DESCRIPTOR = _CHECKFAILURE,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CheckFailure)
  ))
_sym_db.RegisterMessage(CheckFailure)

DiffRequest = _reflection.GeneratedProtocolMessageType('DiffRequest', (_message.Message,), dict(
  DESCRIPTOR = _DIFFREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.DiffRequest)
  ))
_sym_db.RegisterMessage(DiffRequest)

DiffResponse = _reflection.GeneratedProtocolMessageType('DiffResponse', (_message.Message,), dict(
  DESCRIPTOR = _DIFFRESPONSE,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.DiffResponse)
  ))
_sym_db.RegisterMessage(DiffResponse)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATERESPONSE,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CreateResponse)
  ))
_sym_db.RegisterMessage(CreateResponse)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _READREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadRequest)
  ))
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), dict(
  DESCRIPTOR = _READRESPONSE,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadResponse)
  ))
_sym_db.RegisterMessage(ReadResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.UpdateRequest)
  ))
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATERESPONSE,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.UpdateResponse)
  ))
_sym_db.RegisterMessage(UpdateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)


_CONFIGUREREQUEST_VARIABLESENTRY.has_options = True
_CONFIGUREREQUEST_VARIABLESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_RESOURCEPROVIDER = _descriptor.ServiceDescriptor(
  name='ResourceProvider',
  full_name='pulumirpc.ResourceProvider',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1709,
  serialized_end=2298,
  methods=[
  _descriptor.MethodDescriptor(
    name='Configure',
    full_name='pulumirpc.ResourceProvider.Configure',
    index=0,
    containing_service=None,
    input_type=_CONFIGUREREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Invoke',
    full_name='pulumirpc.ResourceProvider.Invoke',
    index=1,
    containing_service=None,
    input_type=_INVOKEREQUEST,
    output_type=_INVOKERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Check',
    full_name='pulumirpc.ResourceProvider.Check',
    index=2,
    containing_service=None,
    input_type=_CHECKREQUEST,
    output_type=_CHECKRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Diff',
    full_name='pulumirpc.ResourceProvider.Diff',
    index=3,
    containing_service=None,
    input_type=_DIFFREQUEST,
    output_type=_DIFFRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='pulumirpc.ResourceProvider.Create',
    index=4,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='pulumirpc.ResourceProvider.Read',
    index=5,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='pulumirpc.ResourceProvider.Update',
    index=6,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='pulumirpc.ResourceProvider.Delete',
    index=7,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPluginInfo',
    full_name='pulumirpc.ResourceProvider.GetPluginInfo',
    index=8,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=plugin__pb2._PLUGININFO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCEPROVIDER)

DESCRIPTOR.services_by_name['ResourceProvider'] = _RESOURCEPROVIDER

# @@protoc_insertion_point(module_scope)
