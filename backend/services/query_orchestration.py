from services.utils.db_executor import execute_query
from services.db_services.db import DB
from .utils.query_generation import generate_sql
from .utils.sql_validator import validate_sql
from .llms.factory import get_llm

def perform_query(db: DB, query: str) -> dict:
    llm = get_llm()
    generatedSql=generate_sql(llm,db.schema,query)
    if not validate_sql(generatedSql):
        raise ValueError("Generated SQL is not valid or safe.")
    print("Generated SQL:", generatedSql)
    results = execute_query(db, generatedSql)
    return {
        "sqlQuery": generatedSql,
        "result": results
    }