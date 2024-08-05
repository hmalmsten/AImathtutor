# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import model_pb2 as model__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in model_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ModelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.predict = channel.unary_unary(
                '/Model/predict',
                request_serializer=model__pb2.modelRequest.SerializeToString,
                response_deserializer=model__pb2.Empty.FromString,
                _registered_method=True)
        self.sendPrediction = channel.unary_stream(
                '/Model/sendPrediction',
                request_serializer=model__pb2.Empty.SerializeToString,
                response_deserializer=model__pb2.modelAnswer.FromString,
                _registered_method=True)
        self.publishMetrics = channel.unary_unary(
                '/Model/publishMetrics',
                request_serializer=model__pb2.metricsJson.SerializeToString,
                response_deserializer=model__pb2.Empty.FromString,
                _registered_method=True)
        self.registerModel = channel.unary_unary(
                '/Model/registerModel',
                request_serializer=model__pb2.Empty.SerializeToString,
                response_deserializer=model__pb2.modelDefinition.FromString,
                _registered_method=True)


class ModelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendPrediction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def publishMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'predict': grpc.unary_unary_rpc_method_handler(
                    servicer.predict,
                    request_deserializer=model__pb2.modelRequest.FromString,
                    response_serializer=model__pb2.Empty.SerializeToString,
            ),
            'sendPrediction': grpc.unary_stream_rpc_method_handler(
                    servicer.sendPrediction,
                    request_deserializer=model__pb2.Empty.FromString,
                    response_serializer=model__pb2.modelAnswer.SerializeToString,
            ),
            'publishMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.publishMetrics,
                    request_deserializer=model__pb2.metricsJson.FromString,
                    response_serializer=model__pb2.Empty.SerializeToString,
            ),
            'registerModel': grpc.unary_unary_rpc_method_handler(
                    servicer.registerModel,
                    request_deserializer=model__pb2.Empty.FromString,
                    response_serializer=model__pb2.modelDefinition.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Model', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Model', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Model(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Model/predict',
            model__pb2.modelRequest.SerializeToString,
            model__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def sendPrediction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/Model/sendPrediction',
            model__pb2.Empty.SerializeToString,
            model__pb2.modelAnswer.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def publishMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Model/publishMetrics',
            model__pb2.metricsJson.SerializeToString,
            model__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def registerModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Model/registerModel',
            model__pb2.Empty.SerializeToString,
            model__pb2.modelDefinition.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
