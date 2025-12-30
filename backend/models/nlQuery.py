from pydantic import BaseModel
from typing import Any

class NLQueryRequest(BaseModel):
    prompt: str

class NLQueryResponse(BaseModel):
    prompt: str
    sqlQuery: str
    result: list[dict[str, Any]]