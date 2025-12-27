from sqlalchemy import text
from sqlalchemy.engine import Engine

from services.schema_manager.schema_prompt_adapter.schema_prompt_adapter import SchemaPromptAdapter

from ..schema_manager.schema_introspector.protocol import SchemaIntrospector
from ..schema_manager.schema_normalizer.protocol import SchemaNormalizer

class DB:
    def __init__(
        self,
        engine: Engine,
        introspector: SchemaIntrospector,
        normalizer: SchemaNormalizer,
    ):
        self.engine = engine
        self.introspector = introspector
        self.normalizer = normalizer
        self.llm_adapter=SchemaPromptAdapter()

        raw_schema = self.introspector.introspect()
        normalized_schema =self.normalizer.normalize(raw_schema)
        llm_friendly_schema = self.llm_adapter.adapt_to_prompt(normalized_schema)
        print(llm_friendly_schema)
        self.schema = llm_friendly_schema

    def execute_readonly_query(self, query: str) -> list[dict]:
        with self.engine.connect() as conn:
            result = conn.execute(text(query))
            return result.mappings().all()
