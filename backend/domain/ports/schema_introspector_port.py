from typing import Protocol

class SchemaIntrospectorPort(Protocol):
    dialect: str
    """
        Returns RAW schema metadata.
        Shape is DB-specific.
        """
    def introspect(self) -> dict:...