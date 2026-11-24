from concurrent import futures
import grpc
import hello_pb2
import hello_pb2_grpc

class GreeterServicer(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Server received request from: {request.name}")
        return hello_pb2.HelloReply(message=f"Hello {request.name} from gRPC Server!")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("gRPC Server running on port 50051...")
server.wait_for_termination()