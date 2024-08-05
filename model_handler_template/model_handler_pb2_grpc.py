# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import model_handler_pb2 as model__handler__pb2

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
        + f' but the generated code in model_handler_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ModelHandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.startTask = channel.unary_unary(
                '/ModelHandler/startTask',
                request_serializer=model__handler__pb2.modelRequirements.SerializeToString,
                response_deserializer=model__handler__pb2.Empty.FromString,
                _registered_method=True)
        self.finishTask = channel.unary_unary(
                '/ModelHandler/finishTask',
                request_serializer=model__handler__pb2.taskMetrics.SerializeToString,
                response_deserializer=model__handler__pb2.metricsJson.FromString,
                _registered_method=True)
        self.sendToModel = channel.unary_unary(
                '/ModelHandler/sendToModel',
                request_serializer=model__handler__pb2.taskRequest.SerializeToString,
                response_deserializer=model__handler__pb2.modelRequest.FromString,
                _registered_method=True)
        self.returnToTask = channel.unary_unary(
                '/ModelHandler/returnToTask',
                request_serializer=model__handler__pb2.modelAnswer.SerializeToString,
                response_deserializer=model__handler__pb2.modelAnswer.FromString,
                _registered_method=True)
        self.registerModel = channel.unary_unary(
                '/ModelHandler/registerModel',
                request_serializer=model__handler__pb2.modelDefinition.SerializeToString,
                response_deserializer=model__handler__pb2.Empty.FromString,
                _registered_method=True)


class ModelHandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def startTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def finishTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendToModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def returnToTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'startTask': grpc.unary_unary_rpc_method_handler(
                    servicer.startTask,
                    request_deserializer=model__handler__pb2.modelRequirements.FromString,
                    response_serializer=model__handler__pb2.Empty.SerializeToString,
            ),
            'finishTask': grpc.unary_unary_rpc_method_handler(
                    servicer.finishTask,
                    request_deserializer=model__handler__pb2.taskMetrics.FromString,
                    response_serializer=model__handler__pb2.metricsJson.SerializeToString,
            ),
            'sendToModel': grpc.unary_unary_rpc_method_handler(
                    servicer.sendToModel,
                    request_deserializer=model__handler__pb2.taskRequest.FromString,
                    response_serializer=model__handler__pb2.modelRequest.SerializeToString,
            ),
            'returnToTask': grpc.unary_unary_rpc_method_handler(
                    servicer.returnToTask,
                    request_deserializer=model__handler__pb2.modelAnswer.FromString,
                    response_serializer=model__handler__pb2.modelAnswer.SerializeToString,
            ),
            'registerModel': grpc.unary_unary_rpc_method_handler(
                    servicer.registerModel,
                    request_deserializer=model__handler__pb2.modelDefinition.FromString,
                    response_serializer=model__handler__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ModelHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ModelHandler', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ModelHandler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def startTask(request,
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
            '/ModelHandler/startTask',
            model__handler__pb2.modelRequirements.SerializeToString,
            model__handler__pb2.Empty.FromString,
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
    def finishTask(request,
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
            '/ModelHandler/finishTask',
            model__handler__pb2.taskMetrics.SerializeToString,
            model__handler__pb2.metricsJson.FromString,
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
    def sendToModel(request,
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
            '/ModelHandler/sendToModel',
            model__handler__pb2.taskRequest.SerializeToString,
            model__handler__pb2.modelRequest.FromString,
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
    def returnToTask(request,
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
            '/ModelHandler/returnToTask',
            model__handler__pb2.modelAnswer.SerializeToString,
            model__handler__pb2.modelAnswer.FromString,
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
            '/ModelHandler/registerModel',
            model__handler__pb2.modelDefinition.SerializeToString,
            model__handler__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
