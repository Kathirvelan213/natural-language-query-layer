from fastapi import APIRouter

router=APIRouter()

@router.get("/query")
def query_response():
    return {"message":"This is a query response"}