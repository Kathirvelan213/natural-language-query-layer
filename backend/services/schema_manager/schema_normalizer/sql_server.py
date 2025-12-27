# schema/normalizers/sql_server.py

SQLSERVER_TYPE_MAP = {
    "int": "int",
    "bigint": "int",
    "smallint": "int",
    "tinyint": "int",
    "bit": "bool",

    "varchar": "text",
    "nvarchar": "text",
    "char": "text",
    "nchar": "text",
    "text": "text",

    "datetime": "timestamp",
    "datetime2": "timestamp",
    "smalldatetime": "timestamp",
    "date": "date",
    "time": "time",

    "decimal": "numeric",
    "numeric": "numeric",
    "money": "numeric",
    "float": "float",
    "real": "float"
}
class SQLServerSchemaNormalizer:
    def normalize(self, raw_schema: dict) -> dict:
        normalized = {"tables": {}}

        for table, columns in raw_schema.items():
            table_entry = {"columns": {}}

            for column, data_type in columns:
                dt = data_type.lower()
                normalized_type = SQLSERVER_TYPE_MAP.get(dt, "text")

                table_entry["columns"][column] = normalized_type

            normalized["tables"][table] = table_entry

        return normalized

