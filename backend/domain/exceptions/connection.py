
class ConnectionError(Exception):
    """Base class for connection-related errors"""

class ConnectionNotFoundError(ConnectionError):
    def __init__(self, conn_id: str):
        super().__init__(f"Connection '{conn_id}' does not exist")
        self.conn_id = conn_id