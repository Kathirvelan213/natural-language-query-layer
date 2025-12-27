from typing import Protocol

class SchemaNormalizer(Protocol):
    dialect: str

    def normalize(self, raw_schema: dict) -> dict:
        ...
