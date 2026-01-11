from typing import Dict
from domain.ports.db_provider_port import DbProviderPort
from domain.ports.schema_introspector_port import SchemaIntrospectorPort
from domain.ports.schema_normalizer_port import SchemaNormalizerPort
from domain.logic import schema_prompt_adapter 
from domain.exceptions.schema import SchemaNotInitializedError

class SchemaManager:
    def __init__(self):
        # conn_id -> Schema
        self._schemas: Dict[str, str] = {}
    
    def store_schema(self, db_provider: DbProviderPort, conn_id:str) -> str:
        introspector:SchemaIntrospectorPort=db_provider.schema_introspector
        normalizer:SchemaNormalizerPort=db_provider.schema_normalizer
        
        introspected_schema=introspector.introspect()
        normalized_schema=normalizer.normalize(introspected_schema)
        schema=schema_prompt_adapter.adapt_to_prompt(normalized_schema)
        self._schemas[conn_id] = schema
        return conn_id
    
    def get_schema(self, conn_id: str):
        if conn_id not in self._schemas:
            raise SchemaNotInitializedError(conn_id)
        return self._schemas.get(conn_id)
    
    def remove_schema(self, conn_id: str) -> bool:
        if conn_id in self._schemas:
            del self._schemas[conn_id]
            return True
        return False
