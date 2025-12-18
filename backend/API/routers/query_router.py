from fastapi import APIRouter

from models.nlQuery import NLQueryResponse, NLQueryRequest
from services.nl_to_sql import generate_sql

router=APIRouter()


@router.post("/query", response_model=NLQueryResponse)
def nl_to_sql(req: NLQueryRequest):
    sql = generate_sql(req.question)

    return {
        "question": req.question,
        "sql": sql
    }