from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from .urls import build_mssql_url, build_postgres_url, build_mysql_url


_URL_BUILDERS= {
    "sqlserver": build_mssql_url,
    "postgres": build_postgres_url,
    "mysql": build_mysql_url,
}

def get_engine(db_type: str, config: dict) -> Engine:
    builder = _URL_BUILDERS.get(db_type)
    if not builder:
        raise ValueError(f"Unsupported database type: {db_type}")

    url = builder(config)
    return create_engine(
        url,
        pool_pre_ping=config.get("pool_pre_ping", True),
    )
