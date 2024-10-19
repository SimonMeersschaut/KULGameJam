class Connection:
    """Represents a connection between the client and the server."""
    def __init__(self):
        assert self.ping_server
    
    def ping_server(self):
        """Returns if the server responds to a ping."""
        ...
    
    def send_packet(self, packet: dict) -> dict:
        """Send a packet to the server."""
        ...
    
    def clear_buffer(self) -> list[dict]:
        """Return received packets."""
        ...