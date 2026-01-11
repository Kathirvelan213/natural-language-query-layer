from typing import Any,List

class ChatBlock():
    def __init__(self,prompt: str,sqlQuery: str,result: list[dict[str, Any]]):
        self.prompt=prompt
        self.sqlQuery=sqlQuery
        self.result=result
        
class Chat:
    def __init__(
        self, chat_id: str, chat_name: str, query_responses: List[ChatBlock]):
        self.chat_id = chat_id
        self.chat_name = chat_name
        self.query_responses = query_responses
        
class ChatSummary:
    def __init__(self, chat_id: str, chat_name: str):
        self.chat_id = chat_id
        self.chat_name = chat_name