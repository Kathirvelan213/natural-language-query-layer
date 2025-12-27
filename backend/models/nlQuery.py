from pydantic import BaseModel
from typing import Any

class NLQueryRequest(BaseModel):
    question: str

class NLQueryResponse(BaseModel):
    question: str
    sql: str
    results: list[dict[str, Any]]