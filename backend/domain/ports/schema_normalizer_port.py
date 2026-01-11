from typing import Protocol

class SchemaNormalizerPort(Protocol):
    dialect: str

    def normalize(self, raw_schema: dict) -> dict:
        ...
