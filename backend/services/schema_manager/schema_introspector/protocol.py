from typing import Protocol

class SchemaIntrospector(Protocol):
    dialect: str
    """
        Returns RAW schema metadata.
        Shape is DB-specific.
        """
    def introspect(self) -> dict:...