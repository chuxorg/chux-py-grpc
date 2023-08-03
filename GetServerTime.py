import grpc

# import the generated classes
import time_service_pb2
import time_service_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = time_service_pb2_grpc.TimeServiceStub(channel)

# create a valid request message
time_request = time_service_pb2.TimeRequest()

# make the call
response = stub.GetServerTime(time_request)

print("Server time is: ", response.server_time)
