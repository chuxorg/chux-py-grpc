# Python gRPC Tutorial: Time Service

This project is a simple demonstration of using gRPC with Python. We'll implement a time service where the client can request the current server time.

The project contains two main Python scripts: a server and a client. The server creates a gRPC service that provides the current server time. The client connects to this service and prints out the server time.

## Prerequisites

- Python 3.11.3 installed. You can download it from [Python's official website](https://www.python.org/downloads/).

## Setup

1. Clone the repository.

```bash
git clone https://github.com/chuxorg/chux-py-grpc.git
cd chux-py-grpc
```

2. Install the required packages.

Create a virtual environment (optional but recommended):

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Run the server.

```bash
python server.py
```

The server will start and listen on port 50051.

2. In another terminal window, run the client.

```bash
python client.py
```

The client will connect to the server and print out the current server time.

## Project Structure

- `server.py`: Contains the Python gRPC server. The server implements a simple service that provides the current server time.
- `client.py`: Contains the Python gRPC client. The client connects to the server and prints out the server time.
- `time_service.proto`: The Protocol Buffers file that defines the `TimeService` service and the `TimeRequest` and `TimeResponse` message types.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)




