import socket

HOST = '127.0.0.1' # "94.225.3.78" # ip of the server
PORT = 8080  # Port to listen on

class Connection:
    """Represents a connection between the client and the server."""
    def __init__(self):
        self.connect()
        # assert self.ping_server()
    
    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b"Hello, world")
            data = s.recv(1024)
            print(data)
    
    def ping_server(self):
        """Returns if the server responds to a ping."""
        ...
    
    def send_packet(self, packet: dict) -> dict:
        """Send a packet to the server."""
        ...
    
    def clear_buffer(self) -> list[dict]:
        """Return received packets."""
        ...

if __name__ == '__main__':
    conn = Connection()