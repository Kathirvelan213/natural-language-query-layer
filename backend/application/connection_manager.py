import uuid
from typing import Dict
from domain.ports.db_provider_factory_port import DbProviderFactoryPort
from domain.exceptions.connection import ConnectionNotFoundError
from domain.exceptions.schema import SchemaNotInitializedError
from domain.ports.db_executor_port import DbExecutorPort


class ConnectionManager:
    def __init__(self, db_provider_factory: DbProviderFactoryPort, schema_manager=None):
        # conn_id -> DbExecutor
        self._connections: Dict[str, DbExecutorPort] = {}
        self._db_provider_factory = db_provider_factory
        self._schema_manager = schema_manager
    
    def create_connection(self, db_type: str, connection_params: dict) -> str:
        db_provider = self._db_provider_factory.get_db_provider(db_type, connection_params)
        executor=db_provider.db_executor
        
        conn_id = str(uuid.uuid4())
        self._connections[conn_id] = executor
        
        if self._schema_manager:
            self._schema_manager.store_schema(db_provider, conn_id)
        return conn_id
    
    def get_connection_executor(self, conn_id: str) -> DbExecutorPort:
        if conn_id not in self._connections:
            raise ConnectionNotFoundError(conn_id)
        if self._schema_manager:
            try:
                self._schema_manager.get_schema(conn_id)
            except SchemaNotInitializedError as schemaNotInitialized:
                raise schemaNotInitialized
        return self._connections.get(conn_id)
    
    def remove_connection(self, conn_id: str) -> bool:
        if conn_id in self._connections:
            del self._connections[conn_id]
            
            if self._schema_manager:
                self._schema_manager.remove_schema(conn_id)
            
            return True
        return False

