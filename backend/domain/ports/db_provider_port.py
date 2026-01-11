from typing import Protocol
from .db_executor_port import DbExecutorPort
from .schema_introspector_port import SchemaIntrospectorPort
from .schema_normalizer_port import SchemaNormalizerPort

class DbProviderPort(Protocol):
    db_executor:DbExecutorPort
    schema_introspector:SchemaIntrospectorPort
    schema_normalizer:SchemaNormalizerPort