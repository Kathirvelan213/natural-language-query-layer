from fastapi import APIRouter,Request,HTTPException
import uuid
import time

from services.db_services.factory import get_database
from models.nlQuery import NLQueryResponse, NLQueryRequest
from services.query_orchestration import perform_query
from api.sessions.db_session import DB_STORE, get_db_from_session
from services.redis_service.chat_store import add_chat_block
router=APIRouter()

@router.post("/connect")
def connect_db(request: Request):
    db = get_database("sqlserver")
    DB_STORE[id(db)] = db
    request.session["db_id"] = id(db)
    
@router.post("/query", response_model=NLQueryResponse)
def nl_to_sql(request: Request, req: NLQueryRequest):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    db=get_db_from_session(request)
    output = perform_query(db, req.prompt)

    result=NLQueryResponse(
        prompt= req.prompt,
        sqlQuery= output["sqlQuery"],
        result= output["result"]
    )
    add_chat_block(user_id,req.chatId,result)
    return result