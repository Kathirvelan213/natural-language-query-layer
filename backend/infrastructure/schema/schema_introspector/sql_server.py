from sqlalchemy import text, Engine
from domain.ports.schema_introspector_port import SchemaIntrospectorPort

class SQLServerSchemaIntrospector(SchemaIntrospectorPort):
    dialect = "sqlserver"

    def __init__(self, engine: Engine, schema: str = "dbo"):
        self.engine = engine
        self.schema = schema

    def introspect(self) -> dict:
        query = text("""
            SELECT
                TABLE_NAME,
                COLUMN_NAME,
                DATA_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = :schema
            ORDER BY TABLE_NAME, ORDINAL_POSITION
        """)

        with self.engine.connect() as conn:
            rows = conn.execute(query, {"schema": self.schema}).all()

        # RAW output (DB-specific)
        schema: dict[str, list[tuple[str, str]]] = {}

        for table, column, data_type in rows:
            schema.setdefault(table, []).append((column, data_type))

        return schema
