# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/cloud/audit/v1/data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/events/cloud/audit/v1/data.proto',
  package='google.events.cloud.audit.v1',
  syntax='proto3',
  serialized_options=b'\252\002%Google.Events.Protobuf.Cloud.Audit.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'google/events/cloud/audit/v1/data.proto\x12\x1cgoogle.events.cloud.audit.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto\"\xf9\x03\n\x0c\x41uditLogData\x12\x14\n\x0cservice_name\x18\x07 \x01(\t\x12\x13\n\x0bmethod_name\x18\x08 \x01(\t\x12\x15\n\rresource_name\x18\x0b \x01(\t\x12\x1a\n\x12num_response_items\x18\x0c \x01(\x03\x12\"\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.Status\x12M\n\x13\x61uthentication_info\x18\x03 \x01(\x0b\x32\x30.google.events.cloud.audit.v1.AuthenticationInfo\x12K\n\x12\x61uthorization_info\x18\t \x03(\x0b\x32/.google.events.cloud.audit.v1.AuthorizationInfo\x12G\n\x10request_metadata\x18\x04 \x01(\x0b\x32-.google.events.cloud.audit.v1.RequestMetadata\x12(\n\x07request\x18\x10 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08response\x18\x11 \x01(\x0b\x32\x17.google.protobuf.Struct\x12-\n\x0cservice_data\x18\x0f \x01(\x0b\x32\x17.google.protobuf.Struct\"-\n\x12\x41uthenticationInfo\x12\x17\n\x0fprincipal_email\x18\x01 \x01(\t\"J\n\x11\x41uthorizationInfo\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x12\n\npermission\x18\x02 \x01(\t\x12\x0f\n\x07granted\x18\x03 \x01(\x08\"H\n\x0fRequestMetadata\x12\x11\n\tcaller_ip\x18\x01 \x01(\t\x12\"\n\x1a\x63\x61ller_supplied_user_agent\x18\x02 \x01(\tB(\xaa\x02%Google.Events.Protobuf.Cloud.Audit.V1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_AUDITLOGDATA = _descriptor.Descriptor(
  name='AuditLogData',
  full_name='google.events.cloud.audit.v1.AuditLogData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='google.events.cloud.audit.v1.AuditLogData.service_name', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='google.events.cloud.audit.v1.AuditLogData.method_name', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.events.cloud.audit.v1.AuditLogData.resource_name', index=2,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_response_items', full_name='google.events.cloud.audit.v1.AuditLogData.num_response_items', index=3,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.events.cloud.audit.v1.AuditLogData.status', index=4,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authentication_info', full_name='google.events.cloud.audit.v1.AuditLogData.authentication_info', index=5,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authorization_info', full_name='google.events.cloud.audit.v1.AuditLogData.authorization_info', index=6,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_metadata', full_name='google.events.cloud.audit.v1.AuditLogData.request_metadata', index=7,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='google.events.cloud.audit.v1.AuditLogData.request', index=8,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='google.events.cloud.audit.v1.AuditLogData.response', index=9,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_data', full_name='google.events.cloud.audit.v1.AuditLogData.service_data', index=10,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=634,
)


_AUTHENTICATIONINFO = _descriptor.Descriptor(
  name='AuthenticationInfo',
  full_name='google.events.cloud.audit.v1.AuthenticationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='principal_email', full_name='google.events.cloud.audit.v1.AuthenticationInfo.principal_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=681,
)


_AUTHORIZATIONINFO = _descriptor.Descriptor(
  name='AuthorizationInfo',
  full_name='google.events.cloud.audit.v1.AuthorizationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='google.events.cloud.audit.v1.AuthorizationInfo.resource', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permission', full_name='google.events.cloud.audit.v1.AuthorizationInfo.permission', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='granted', full_name='google.events.cloud.audit.v1.AuthorizationInfo.granted', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=683,
  serialized_end=757,
)


_REQUESTMETADATA = _descriptor.Descriptor(
  name='RequestMetadata',
  full_name='google.events.cloud.audit.v1.RequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='caller_ip', full_name='google.events.cloud.audit.v1.RequestMetadata.caller_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='caller_supplied_user_agent', full_name='google.events.cloud.audit.v1.RequestMetadata.caller_supplied_user_agent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=831,
)

_AUDITLOGDATA.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_AUDITLOGDATA.fields_by_name['authentication_info'].message_type = _AUTHENTICATIONINFO
_AUDITLOGDATA.fields_by_name['authorization_info'].message_type = _AUTHORIZATIONINFO
_AUDITLOGDATA.fields_by_name['request_metadata'].message_type = _REQUESTMETADATA
_AUDITLOGDATA.fields_by_name['request'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_AUDITLOGDATA.fields_by_name['response'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_AUDITLOGDATA.fields_by_name['service_data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['AuditLogData'] = _AUDITLOGDATA
DESCRIPTOR.message_types_by_name['AuthenticationInfo'] = _AUTHENTICATIONINFO
DESCRIPTOR.message_types_by_name['AuthorizationInfo'] = _AUTHORIZATIONINFO
DESCRIPTOR.message_types_by_name['RequestMetadata'] = _REQUESTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuditLogData = _reflection.GeneratedProtocolMessageType('AuditLogData', (_message.Message,), {
  'DESCRIPTOR' : _AUDITLOGDATA,
  '__module__' : 'google.events.cloud.audit.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.audit.v1.AuditLogData)
  })
_sym_db.RegisterMessage(AuditLogData)

AuthenticationInfo = _reflection.GeneratedProtocolMessageType('AuthenticationInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONINFO,
  '__module__' : 'google.events.cloud.audit.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.audit.v1.AuthenticationInfo)
  })
_sym_db.RegisterMessage(AuthenticationInfo)

AuthorizationInfo = _reflection.GeneratedProtocolMessageType('AuthorizationInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONINFO,
  '__module__' : 'google.events.cloud.audit.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.audit.v1.AuthorizationInfo)
  })
_sym_db.RegisterMessage(AuthorizationInfo)

RequestMetadata = _reflection.GeneratedProtocolMessageType('RequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMETADATA,
  '__module__' : 'google.events.cloud.audit.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.audit.v1.RequestMetadata)
  })
_sym_db.RegisterMessage(RequestMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
