from pydantic import BaseModel
from typing import Any

class QueryRequest(BaseModel):
    chatId:str
    prompt: str

class QueryResponse(BaseModel):
    prompt: str
    sqlQuery: str
    result: list[dict[str, Any]]