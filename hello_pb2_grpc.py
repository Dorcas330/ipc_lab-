import grpc
import hello_pb2

class GreeterStub:
    def __init__(self, channel):
        self.SayHello = channel.unary_unary(
            '/Greeter/SayHello',
            request_serializer=hello_pb2.HelloRequest.SerializeToString,
            response_deserializer=hello_pb2.HelloReply.FromString,
        )

class GreeterServicer:
    def SayHello(self, request, context):
        raise NotImplementedError('Method not implemented!')

def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SayHello': grpc.unary_unary_rpc_method_handler(
            servicer.SayHello,
            request_deserializer=hello_pb2.HelloRequest.FromString,
            response_serializer=hello_pb2.HelloReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler('Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))