from fastapi import APIRouter,Request,HTTPException

from api.models.query import QueryResponse, QueryRequest
from api.models.connection import DbConnectionParams
from _bootstrap import get_query_manager, get_connection_manager, get_chat_manager
 
router=APIRouter()

@router.post("/{chat_id}/connect")
def connect_db(request: Request, chat_id: str,db_type:str, params: DbConnectionParams):
    """Create database connection and store connection ID in chat metadata"""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    try:
        # Connection manager handles engine creation and storage
        conn_manager = get_connection_manager()
        conn_id = conn_manager.create_connection(db_type, params)
        
        # Store conn_id in Redis chat metadata
        chat_manager = get_chat_manager()
        chat_manager.save_connection_id(user_id, chat_id, conn_id)
        
        return {"message": "Connection established"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to connect: {str(e)}")

@router.post("/query", response_model=QueryResponse)
def nl_to_sql(request: Request, req: QueryRequest):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Get connection ID for this chat
    chat_manager = get_chat_manager()
    conn_id = chat_manager.get_connection_id(user_id, req.chatId)
    if not conn_id:
        raise HTTPException(status_code=400, detail="Database not connected for this chat")
    
    # Fetch engine from connection manager
    conn_manager = get_connection_manager()
    db = conn_manager.get_connection_executor(conn_id)
    if not db:
        raise HTTPException(status_code=400, detail="Connection not found or expired")
    
    query_manger=get_query_manager()
    output = query_manger.perform_query(db, req.prompt, conn_id)

    result=QueryResponse(
        prompt= req.prompt,
        sqlQuery= output["sqlQuery"],
        result= output["result"]
    )
    chat_manager.add_chat_block(user_id, req.chatId, result)
    return result