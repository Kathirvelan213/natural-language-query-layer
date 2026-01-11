from typing import Protocol

class DbExecutorPort(Protocol):
    def execute_readonly_query(self, query: str) -> list[dict]: ...