from pydantic import BaseModel
from typing import List, Optional
from .nlQuery import NLQueryResponse

class Chat(BaseModel):
    chatId: str
    chatName: str
    queryResponses: List[NLQueryResponse]

class ChatSummary(BaseModel):
    chat_id: str
    chat_name: str

class CreateChatRequest(BaseModel):
    chat_name: Optional[str] = "New Chat"