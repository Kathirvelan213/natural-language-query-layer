from fastapi import APIRouter, Request, HTTPException
from typing import List
import uuid
import time
from api.models.chat import Chat, ChatSummary, CreateChatRequest
from _bootstrap import get_chat_manager

router = APIRouter()

@router.get("/", response_model=List[ChatSummary])
def get_all_user_chats(request: Request):
    """Get all chats for the current user"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        return []
    
    chat_manager = get_chat_manager()
    return chat_manager.list_user_chats(user_id)


@router.post("/", response_model=ChatSummary)
def create_new_chat(request: Request, chat_request: CreateChatRequest):
    """Create a new chat with database connection"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        # Create anonymous user session on first chat creation
        user_id = f"anon_{uuid.uuid4()}"
        request.session["user_id"] = user_id
        request.session["is_authenticated"] = False
        request.session["created_at"] = time.time()
    
    try:
        chat_manager = get_chat_manager()
        chat_name = chat_request.chat_name if chat_request.chat_name else "New Chat"
        return chat_manager.create_chat(
            user_id,
            chat_name,
            chat_request.db_type,
            chat_request.connection_params.model_dump()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create chat: {str(e)}")


@router.get("/{chat_id}", response_model=Chat)
def get_chat(request: Request, chat_id: str):
    """Get chat history for a specific chat"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    chat_manager = get_chat_manager()
    chat_data = chat_manager.get_chat(user_id, chat_id)
    if chat_data is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return Chat(**chat_data)


@router.delete("/{chat_id}")
def delete_user_chat(request: Request, chat_id: str):
    """Delete a specific chat"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    chat_manager = get_chat_manager()
    success = chat_manager.delete_chat(user_id, chat_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    return {"message": "Chat deleted successfully"}
    

