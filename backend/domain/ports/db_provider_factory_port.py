from typing import Protocol
from .db_provider_port import DbProviderPort

class DbProviderFactoryPort(Protocol):
    def get_db_provider(dbType:str,config:dict) -> DbProviderPort:...