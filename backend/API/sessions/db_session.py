from fastapi import Request, HTTPException
from services.db_services.db import DB

DB_STORE = {} 

def get_db_from_session(request: Request) -> DB:
    db_id = request.session.get("db_id")

    if not db_id:
        raise HTTPException(400, "No database connected")

    return DB_STORE[db_id]
