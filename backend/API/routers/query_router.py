from fastapi import APIRouter,Request

from services.db_services.factory import get_database
from models.nlQuery import NLQueryResponse, NLQueryRequest
from services.query_orchestration import perform_query
from api.sessions.db_session import DB_STORE, get_db_from_session
router=APIRouter()

@router.post("/connect")
def connect_db(request: Request):
    db = get_database("sqlserver")
    DB_STORE[id(db)] = db
    request.session["db_id"] = id(db)
    
@router.post("/query", response_model=NLQueryResponse)
def nl_to_sql(request: Request, req: NLQueryRequest):
    db=get_db_from_session(request)
    output = perform_query(db, req.question)

    return {
        "question": req.question,
        "sql": output["sql"],
        "results": output["results"]
    }