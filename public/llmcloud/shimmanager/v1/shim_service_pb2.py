# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public/llmcloud/shimmanager/v1/shim_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1public/llmcloud/shimmanager/v1/shim_service.proto\x12\x1epublic.llmcloud.shimmanager.v1\"A\n\x1aShimServiceGetQueryRequest\x12#\n\rnum_requested\x18\x01 \x01(\rR\x0cnumRequested\"\x85\x02\n\x05Query\x12\x18\n\x05query\x18\x01 \x03(\rB\x02\x10\x01R\x05query\x12\x1d\n\nrequest_id\x18\x02 \x01(\tR\trequestId\x12\x12\n\x04seed\x18\x03 \x01(\rR\x04seed\x12\x1d\n\nmax_tokens\x18\x04 \x01(\rR\tmaxTokens\x12 \n\x0btemperature\x18\x05 \x01(\x02R\x0btemperature\x12\x13\n\x05top_p\x18\x06 \x01(\x02R\x04topP\x12\x13\n\x05top_k\x18\x07 \x01(\rR\x04topK\x12)\n\x10response_address\x18\x08 \x01(\tR\x0fresponseAddress\x12\x19\n\x08model_id\x18\t \x01(\tR\x07modelId\"m\n\x1bShimServiceGetQueryResponse\x12N\n\x0fquery_responses\x18\x01 \x03(\x0b\x32%.public.llmcloud.shimmanager.v1.QueryR\x0equeryResponses2\x95\x01\n\x0bShimService\x12\x85\x01\n\x08GetQuery\x12:.public.llmcloud.shimmanager.v1.ShimServiceGetQueryRequest\x1a;.public.llmcloud.shimmanager.v1.ShimServiceGetQueryResponse\"\x00\x42\x9c\x02\n\"com.public.llmcloud.shimmanager.v1B\x10ShimServiceProtoP\x01ZGgit.groq.io/cloud/go-proto/public/llmcloud/shimmanager/v1;shimmanagerv1\xa2\x02\x03PLS\xaa\x02\x1ePublic.Llmcloud.Shimmanager.V1\xca\x02\x1fPublic_\\Llmcloud\\Shimmanager\\V1\xe2\x02+Public_\\Llmcloud\\Shimmanager\\V1\\GPBMetadata\xea\x02!Public::Llmcloud::Shimmanager::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.llmcloud.shimmanager.v1.shim_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.public.llmcloud.shimmanager.v1B\020ShimServiceProtoP\001ZGgit.groq.io/cloud/go-proto/public/llmcloud/shimmanager/v1;shimmanagerv1\242\002\003PLS\252\002\036Public.Llmcloud.Shimmanager.V1\312\002\037Public_\\Llmcloud\\Shimmanager\\V1\342\002+Public_\\Llmcloud\\Shimmanager\\V1\\GPBMetadata\352\002!Public::Llmcloud::Shimmanager::V1'
  _globals['_QUERY'].fields_by_name['query']._options = None
  _globals['_QUERY'].fields_by_name['query']._serialized_options = b'\020\001'
  _globals['_SHIMSERVICEGETQUERYREQUEST']._serialized_start=85
  _globals['_SHIMSERVICEGETQUERYREQUEST']._serialized_end=150
  _globals['_QUERY']._serialized_start=153
  _globals['_QUERY']._serialized_end=414
  _globals['_SHIMSERVICEGETQUERYRESPONSE']._serialized_start=416
  _globals['_SHIMSERVICEGETQUERYRESPONSE']._serialized_end=525
  _globals['_SHIMSERVICE']._serialized_start=528
  _globals['_SHIMSERVICE']._serialized_end=677
# @@protoc_insertion_point(module_scope)
