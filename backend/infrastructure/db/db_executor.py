from sqlalchemy import text,Engine
from domain.ports.db_executor_port import DbExecutorPort

class DbExecutor(DbExecutorPort):
    def __init__(self, engine:Engine):
        self.engine = engine

    def execute_readonly_query(self, query: str) -> list[dict]:
        with self.engine.connect() as conn:
            result = conn.execute(text(query))
            return result.mappings().all()
