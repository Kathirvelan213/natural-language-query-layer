from domain.ports.db_executor_port import DbExecutorPort
from domain.ports.db_provider_port import DbProviderPort
from domain.ports.schema_introspector_port import SchemaIntrospectorPort
from domain.ports.schema_normalizer_port import SchemaNormalizerPort

class DbProvider(DbProviderPort):
    def __init__(self,
        db_executor:DbExecutorPort,
        schema_introspector:SchemaIntrospectorPort,
        schema_normalizer:SchemaNormalizerPort
    ) :
        self.db_executor=db_executor
        self.schema_introspector=schema_introspector
        self.schema_normalizer=schema_normalizer 