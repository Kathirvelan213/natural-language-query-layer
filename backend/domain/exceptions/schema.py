# domain/exceptions/schema.py

class SchemaError(Exception):
    """Base class for schema-related errors"""

class SchemaNotInitializedError(SchemaError):
    def __init__(self, conn_id: str):
        super().__init__(f"Schema not initialized for connection '{conn_id}'")
        self.conn_id = conn_id
