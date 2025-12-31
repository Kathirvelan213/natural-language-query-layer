from sqlalchemy import Engine, create_engine
import pyodbc
class SqlServerEngine:
    def create(self) -> Engine:
        print(pyodbc.drivers())
        return create_engine(
            "mssql+pyodbc://appTestUser2:Password%401"
            "@host.docker.internal:1433/db-market-access-local"
            "?driver=ODBC+Driver+17+for+SQL+Server"
            "&Encrypt=no",
            pool_pre_ping=True,
        )