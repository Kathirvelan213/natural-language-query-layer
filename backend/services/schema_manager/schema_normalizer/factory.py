from .protocol import SchemaNormalizer
from .sql_server import SQLServerSchemaNormalizer
from sqlalchemy.engine import Engine

def get_schema_normalizer(dbType: str) -> SchemaNormalizer:
    if dbType == "sqlserver":
        return SQLServerSchemaNormalizer()
    else:
        raise ValueError(f"Unsupported dbType: {dbType}")