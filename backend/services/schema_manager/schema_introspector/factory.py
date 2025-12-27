from .protocol import SchemaIntrospector
from .sql_server import SQLServerSchemaIntrospector
from sqlalchemy.engine import Engine

def get_schema_inspector(dbType: str, engine:Engine) -> SchemaIntrospector:
    if dbType == "sqlserver":
        return SQLServerSchemaIntrospector(engine)
    else:
        raise ValueError(f"Unsupported dbType: {dbType}")