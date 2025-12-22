from .utils.query_generation import generate_sql
from .utils.sql_validator import validate_sql

def perform_query(llm, query: str) -> str:
    generatedSql=generate_sql(llm, query)
    if not validate_sql(generatedSql):
        raise ValueError("Generated SQL is not valid or safe.")
    return generatedSql