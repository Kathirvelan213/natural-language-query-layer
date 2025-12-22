from fastapi import APIRouter

from models.nlQuery import NLQueryResponse, NLQueryRequest
from services.query_orchestration import perform_query
from services.llms.factory import get_llm
router=APIRouter()


@router.post("/query", response_model=NLQueryResponse)
def nl_to_sql(req: NLQueryRequest):
    llm = get_llm()
    sql = perform_query(llm, req.question)

    return {
        "question": req.question,
        "sql": sql
    }