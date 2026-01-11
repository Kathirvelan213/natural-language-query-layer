from pydantic import BaseModel
from typing import List, Optional
from api.models.query import QueryResponse
from api.models.connection import DbConnectionParams

class Chat(BaseModel):
    chatId: str
    chatName: str
    queryResponses: List[QueryResponse]

class ChatSummary(BaseModel):
    chat_id: str
    chat_name: str

class CreateChatRequest(BaseModel):
    chat_name: Optional[str] = "New Chat"
    db_type: str
    connection_params: DbConnectionParams