from domain.ports.llm_port import LLMPort
from domain.logic import query_generation, sql_validator
from domain.exceptions.query import UnsafeOrInvalidSQLGeneratedError
from application.schema_manager import SchemaManager
from application.connection_manager import ConnectionManager


class QueryManager:
    def __init__(self, llm: LLMPort, connection_manager: ConnectionManager, schema_manager: SchemaManager):
        self.llm = llm
        self.connection_manager = connection_manager
        self.schema_manager = schema_manager
    
    def perform_query(self, db, query: str, conn_id: str) -> dict:
        schema = self.schema_manager.get_schema(conn_id)
        
        generatedPrompt = query_generation.generate_prompt(schema, query)
        
        generatedSql = self.llm.generate(generatedPrompt)
        
        if not sql_validator.validate_sql(generatedSql):
            raise UnsafeOrInvalidSQLGeneratedError(generatedSql)
        print("Generated SQL:", generatedSql)
        
        results = db.execute_readonly_query(generatedSql)
        return {
            "sqlQuery": generatedSql,
            "result": results
        }