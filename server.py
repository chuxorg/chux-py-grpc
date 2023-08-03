import grpc
from concurrent import futures
import time

# import the generated classes
import time_service_pb2
import time_service_pb2_grpc

# implement the service class
class TimeServiceServicer(time_service_pb2_grpc.TimeServiceServicer):
    # implementation of the GetServerTime rpc method
    def GetServerTime(self, request, context):
        current_time = time.ctime(time.time())
        return time_service_pb2.TimeResponse(server_time=current_time)

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# add the service to the server
time_service_pb2_grpc.add_TimeServiceServicer_to_server(TimeServiceServicer(), server)

# start the server
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# keep the server running
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
