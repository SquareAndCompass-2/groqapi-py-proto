# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from public.llmcloud.globalstatsmanager.v1 import globalstatsmanager_pb2 as public_dot_llmcloud_dot_globalstatsmanager_dot_v1_dot_globalstatsmanager__pb2


class GlobalStatsManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGlobalStats = channel.unary_unary(
                '/public.llmcloud.globalstatsmanager.v1.GlobalStatsManagerService/GetGlobalStats',
                request_serializer=public_dot_llmcloud_dot_globalstatsmanager_dot_v1_dot_globalstatsmanager__pb2.GetGlobalStatsRequest.SerializeToString,
                response_deserializer=public_dot_llmcloud_dot_globalstatsmanager_dot_v1_dot_globalstatsmanager__pb2.GetGlobalStatsResponse.FromString,
                )


class GlobalStatsManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetGlobalStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GlobalStatsManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGlobalStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGlobalStats,
                    request_deserializer=public_dot_llmcloud_dot_globalstatsmanager_dot_v1_dot_globalstatsmanager__pb2.GetGlobalStatsRequest.FromString,
                    response_serializer=public_dot_llmcloud_dot_globalstatsmanager_dot_v1_dot_globalstatsmanager__pb2.GetGlobalStatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'public.llmcloud.globalstatsmanager.v1.GlobalStatsManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GlobalStatsManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetGlobalStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/public.llmcloud.globalstatsmanager.v1.GlobalStatsManagerService/GetGlobalStats',
            public_dot_llmcloud_dot_globalstatsmanager_dot_v1_dot_globalstatsmanager__pb2.GetGlobalStatsRequest.SerializeToString,
            public_dot_llmcloud_dot_globalstatsmanager_dot_v1_dot_globalstatsmanager__pb2.GetGlobalStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
