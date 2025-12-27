from services.db_services.db import DB

def execute_query(db:DB, query:str)->list[dict]:
    return db.execute_readonly_query(query)
    