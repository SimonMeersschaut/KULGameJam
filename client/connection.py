import socket
import json

HOST = '127.0.0.1' # "94.225.3.78" # ip of the server
PORT = 8080  # Port to listen on

class Connection:
    """Represents a connection between the client and the server."""
    def __init__(self):
        connected = self.connect()
        assert connected, "Not connected to the server."
    
    def connect(self):
        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM).__enter__()
            self.conn.connect((HOST, PORT))
            return True
        except ConnectionRefusedError:
            # server is not running
            return False
    
    def send_packet(self, packet: dict) -> dict:
        """Send a packet to the server and read the response."""
        msg = json.dumps(packet).encode('utf-8')
        self.conn.sendall(msg)
        data = self.conn.recv(1024)
        return json.loads(data)
    
if __name__ == '__main__':
    conn = Connection()