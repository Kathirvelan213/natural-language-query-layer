from pydantic import BaseModel


class DbConnectionParams(BaseModel):
    """Database connection parameters"""
    host: str
    port: str
    database: str
    username: str
    password: str

