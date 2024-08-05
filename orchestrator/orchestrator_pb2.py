# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orchestrator.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12orchestrator.proto\"D\n\x0btaskRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\x12\x11\n\tsessionID\x18\x02 \x01(\t\x12\x11\n\tmessageID\x18\x03 \x01(\t\"C\n\x0bmodelAnswer\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\x12\x11\n\tsessionID\x18\x02 \x01(\t\x12\x11\n\tmessageID\x18\x03 \x01(\t\"\x1e\n\tidMessage\x12\x11\n\tsessionID\x18\x01 \x01(\t\"1\n\x0btaskMetrics\x12\x11\n\tsessionID\x18\x01 \x01(\t\x12\x0f\n\x07metrics\x18\x02 \x01(\t\"V\n\x0cmodelRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\x12\x0f\n\x07modelID\x18\x02 \x01(\t\x12\x11\n\tsessionID\x18\x03 \x01(\t\x12\x11\n\tmessageID\x18\x04 \x01(\t\"p\n\x0fmodelDefinition\x12\x12\n\nneeds_text\x18\x01 \x01(\x08\x12\x13\n\x0bneeds_image\x18\x02 \x01(\x08\x12\x10\n\x08\x63\x61n_text\x18\x03 \x01(\x08\x12\x11\n\tcan_image\x18\x04 \x01(\x08\x12\x0f\n\x07modelID\x18\x05 \x01(\t\"O\n\x11modelRequirements\x12\x12\n\nneeds_text\x18\x01 \x01(\x08\x12\x13\n\x0bneeds_image\x18\x02 \x01(\x08\x12\x11\n\tsessionID\x18\x03 \x01(\t\"/\n\x0bmetricsJson\x12\x0f\n\x07metrics\x18\x01 \x01(\t\x12\x0f\n\x07modelID\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\xe4\x01\n\x0cModelHandler\x12\'\n\tstartTask\x12\x12.modelRequirements\x1a\x06.Empty\x12(\n\nfinishTask\x12\x0c.taskMetrics\x1a\x0c.metricsJson\x12*\n\x0bsendToModel\x12\x0c.taskRequest\x1a\r.modelRequest\x12*\n\x0creturnToTask\x12\x0c.modelAnswer\x1a\x0c.modelAnswer\x12)\n\rregisterModel\x12\x10.modelDefinition\x1a\x06.Empty2\xab\x01\n\x0btaskService\x12)\n\tstartTask\x12\x06.Empty\x1a\x12.modelRequirements0\x01\x12!\n\x07runTask\x12\x06.Empty\x1a\x0c.taskRequest0\x01\x12$\n\nfinishTask\x12\x06.Empty\x1a\x0c.taskMetrics0\x01\x12(\n\x10getModelResponse\x12\x0c.modelAnswer\x1a\x06.Empty2\xa6\x01\n\x05Model\x12 \n\x07predict\x12\r.modelRequest\x1a\x06.Empty\x12(\n\x0esendPrediction\x12\x06.Empty\x1a\x0c.modelAnswer0\x01\x12&\n\x0epublishMetrics\x12\x0c.metricsJson\x1a\x06.Empty\x12)\n\rregisterModel\x12\x06.Empty\x1a\x10.modelDefinitionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'orchestrator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TASKREQUEST']._serialized_start=22
  _globals['_TASKREQUEST']._serialized_end=90
  _globals['_MODELANSWER']._serialized_start=92
  _globals['_MODELANSWER']._serialized_end=159
  _globals['_IDMESSAGE']._serialized_start=161
  _globals['_IDMESSAGE']._serialized_end=191
  _globals['_TASKMETRICS']._serialized_start=193
  _globals['_TASKMETRICS']._serialized_end=242
  _globals['_MODELREQUEST']._serialized_start=244
  _globals['_MODELREQUEST']._serialized_end=330
  _globals['_MODELDEFINITION']._serialized_start=332
  _globals['_MODELDEFINITION']._serialized_end=444
  _globals['_MODELREQUIREMENTS']._serialized_start=446
  _globals['_MODELREQUIREMENTS']._serialized_end=525
  _globals['_METRICSJSON']._serialized_start=527
  _globals['_METRICSJSON']._serialized_end=574
  _globals['_EMPTY']._serialized_start=576
  _globals['_EMPTY']._serialized_end=583
  _globals['_MODELHANDLER']._serialized_start=586
  _globals['_MODELHANDLER']._serialized_end=814
  _globals['_TASKSERVICE']._serialized_start=817
  _globals['_TASKSERVICE']._serialized_end=988
  _globals['_MODEL']._serialized_start=991
  _globals['_MODEL']._serialized_end=1157
# @@protoc_insertion_point(module_scope)
