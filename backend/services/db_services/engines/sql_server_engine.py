from sqlalchemy import Engine, create_engine

class SqlServerEngine:
    def create(self) -> Engine:
        return create_engine(
            "mssql+pyodbc://@KATHIRVELAN\\SQLEXPRESS/db-market-access-local"
            "?driver=ODBC+Driver+18+for+SQL+Server"
            "&trusted_connection=yes"
            "&Encrypt=yes"
            "&TrustServerCertificate=yes",
            pool_pre_ping=True,
        )