# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from public.llmcloud.inferencemanager.v1 import inference_result_service_pb2 as public_dot_llmcloud_dot_inferencemanager_dot_v1_dot_inference__result__service__pb2


class InferenceResultServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetResult = channel.stream_unary(
                '/public.llmcloud.inferencemanager.v1.InferenceResultService/GetResult',
                request_serializer=public_dot_llmcloud_dot_inferencemanager_dot_v1_dot_inference__result__service__pb2.InferenceResultServiceGetResultRequest.SerializeToString,
                response_deserializer=public_dot_llmcloud_dot_inferencemanager_dot_v1_dot_inference__result__service__pb2.InferenceResultServiceGetResultResponse.FromString,
                )


class InferenceResultServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetResult(self, request_iterator, context):
        """returns the query at the the top of the priority queue
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InferenceResultServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetResult': grpc.stream_unary_rpc_method_handler(
                    servicer.GetResult,
                    request_deserializer=public_dot_llmcloud_dot_inferencemanager_dot_v1_dot_inference__result__service__pb2.InferenceResultServiceGetResultRequest.FromString,
                    response_serializer=public_dot_llmcloud_dot_inferencemanager_dot_v1_dot_inference__result__service__pb2.InferenceResultServiceGetResultResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'public.llmcloud.inferencemanager.v1.InferenceResultService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InferenceResultService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetResult(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/public.llmcloud.inferencemanager.v1.InferenceResultService/GetResult',
            public_dot_llmcloud_dot_inferencemanager_dot_v1_dot_inference__result__service__pb2.InferenceResultServiceGetResultRequest.SerializeToString,
            public_dot_llmcloud_dot_inferencemanager_dot_v1_dot_inference__result__service__pb2.InferenceResultServiceGetResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
