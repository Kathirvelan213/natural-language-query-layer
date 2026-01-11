# infra/engine/urls.py
from urllib.parse import quote_plus


def build_mssql_url(config: dict) -> str:
    return (
        f"mssql+pyodbc://{config['username']}:{quote_plus(config['password'])}"
        f"@{config['host']}:{config.get('port', 1433)}/{config['database']}"
        f"?driver={quote_plus(config.get('driver', 'ODBC Driver 17 for SQL Server'))}"
        f"&Encrypt={'yes' if config.get('encrypt', False) else 'no'}"
    )


def build_postgres_url(config: dict) -> str:
    return (
        f"postgresql+psycopg2://{config['username']}:{quote_plus(config['password'])}"
        f"@{config['host']}:{config.get('port', 5432)}/{config['database']}"
    )


def build_mysql_url(config: dict) -> str:
    return (
        f"mysql+pymysql://{config['username']}:{quote_plus(config['password'])}"
        f"@{config['host']}:{config.get('port', 3306)}/{config['database']}"
    )
