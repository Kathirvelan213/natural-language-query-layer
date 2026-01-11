class QueryError(Exception):
    """Base class for query-related errors"""

class UnsafeOrInvalidSQLGeneratedError(QueryError):
    def __init__(self, sql: str):
        super().__init__("Generated SQL is invalid or unsafe")
        self.sql = sql