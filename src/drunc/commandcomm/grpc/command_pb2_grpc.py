# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import drunc.commandcomm.grpc.command_pb2 as command__pb2


class CommandReceiverStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecuteCommand = channel.unary_stream(
                '/command.CommandReceiver/ExecuteCommand',
                request_serializer=command__pb2.Command.SerializeToString,
                response_deserializer=command__pb2.CommandResponse.FromString,
                )


class CommandReceiverServicer(object):
    """The greeting service definition.
    """

    def ExecuteCommand(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommandReceiverServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExecuteCommand': grpc.unary_stream_rpc_method_handler(
                    servicer.ExecuteCommand,
                    request_deserializer=command__pb2.Command.FromString,
                    response_serializer=command__pb2.CommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'command.CommandReceiver', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommandReceiver(object):
    """The greeting service definition.
    """

    @staticmethod
    def ExecuteCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/command.CommandReceiver/ExecuteCommand',
            command__pb2.Command.SerializeToString,
            command__pb2.CommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
