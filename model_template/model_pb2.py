# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\"C\n\x0cmodelRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\x12\x0f\n\x07modelID\x18\x02 \x01(\t\x12\x11\n\tsessionID\x18\x03 \x01(\t\"0\n\x0bmodelAnswer\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\x12\x11\n\tsessionID\x18\x02 \x01(\t\"p\n\x0fmodelDefinition\x12\x12\n\nneeds_text\x18\x01 \x01(\x08\x12\x13\n\x0bneeds_image\x18\x02 \x01(\x08\x12\x10\n\x08\x63\x61n_text\x18\x03 \x01(\x08\x12\x11\n\tcan_image\x18\x04 \x01(\x08\x12\x0f\n\x07modelID\x18\x05 \x01(\t\"/\n\x0bmetricsJson\x12\x0f\n\x07metrics\x18\x01 \x01(\t\x12\x0f\n\x07modelID\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\xa6\x01\n\x05Model\x12 \n\x07predict\x12\r.modelRequest\x1a\x06.Empty\x12(\n\x0esendPrediction\x12\x06.Empty\x1a\x0c.modelAnswer0\x01\x12&\n\x0epublishMetrics\x12\x0c.metricsJson\x1a\x06.Empty\x12)\n\rregisterModel\x12\x06.Empty\x1a\x10.modelDefinitionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MODELREQUEST']._serialized_start=15
  _globals['_MODELREQUEST']._serialized_end=82
  _globals['_MODELANSWER']._serialized_start=84
  _globals['_MODELANSWER']._serialized_end=132
  _globals['_MODELDEFINITION']._serialized_start=134
  _globals['_MODELDEFINITION']._serialized_end=246
  _globals['_METRICSJSON']._serialized_start=248
  _globals['_METRICSJSON']._serialized_end=295
  _globals['_EMPTY']._serialized_start=297
  _globals['_EMPTY']._serialized_end=304
  _globals['_MODEL']._serialized_start=307
  _globals['_MODEL']._serialized_end=473
# @@protoc_insertion_point(module_scope)
