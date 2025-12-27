from ..engines.sql_server_engine import SqlServerEngine

def get_Engine(dbType: str):
    if dbType == "sqlserver":
        return SqlServerEngine().create()
    else:
        raise ValueError(f"Unsupported database type: {dbType}")

    
