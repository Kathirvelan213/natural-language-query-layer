from fastapi import APIRouter, Request, HTTPException
from typing import List
import uuid
import time
from models.chat import Chat, ChatSummary, CreateChatRequest
from models.nlQuery import NLQueryResponse
from services.redis_service.chat_store import (
    get_chat_history,
    get_all_chats,
    create_chat,
    delete_chat,
    get_chat_metadata
)
router = APIRouter()


@router.get("/", response_model=List[ChatSummary])
def get_all_user_chats(request: Request):
    """Get all chats for the current user"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        return []
    
    chats = get_all_chats(user_id)
    return chats


@router.post("/", response_model=ChatSummary)
def create_new_chat(request: Request, chat_request: CreateChatRequest = None):
    """Create a new chat"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        # Create anonymous user session on first chat creation
        user_id = f"anon_{uuid.uuid4()}"
        request.session["user_id"] = user_id
        request.session["is_authenticated"] = False
        request.session["created_at"] = time.time()
    
    chat_id = str(uuid.uuid4())
    chat_name = chat_request.chat_name if chat_request and chat_request.chat_name else "New Chat"
    
    chat_summary = create_chat(user_id, chat_id, chat_name)
    return chat_summary


@router.get("/{chat_id}", response_model=Chat)
def get_chat(request: Request, chat_id: str):
    """Get chat history for a specific chat"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    messages = get_chat_history(user_id, chat_id)
    
    if messages is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    # Get chat name from metadata
    chat_name = get_chat_metadata(user_id, chat_id)
    
    return Chat(
        chatId=chat_id,
        chatName=chat_name,
        queryResponses=messages
    )


@router.delete("/{chat_id}")
def delete_user_chat(request: Request, chat_id: str):
    """Delete a specific chat"""
    user_id = request.session.get("user_id")
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    success = delete_chat(user_id, chat_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Chat not found")
    
    return {"message": "Chat deleted successfully"}
    

