import json
import time
import os
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

from domain.ports.chat_cache_port import ChatCachePort
from .redis_client import redis_client

load_dotenv()
CHAT_TTL = int(os.getenv("CHAT_TTL", "86400"))


class ChatCache(ChatCachePort):
    def __init__(self, client=redis_client, ttl: int = CHAT_TTL):
        self.client = client
        self.ttl = ttl

    def add_chat_block(self, user_id: str, chat_id: str, message: Any) -> None:
        key = f"chat:{user_id}:{chat_id}"
        payload = message.model_dump_json() if hasattr(message, "model_dump_json") else json.dumps(message)
        self.client.rpush(key, payload)
        self.client.expire(key, self.ttl)

    def get_chat_history(self, user_id: str, chat_id: str) -> Optional[List[Dict[str, Any]]]:
        key = f"chat:{user_id}:{chat_id}"
        if not self.client.exists(key):
            return None
        messages = self.client.lrange(key, 0, -1)
        return [json.loads(message) for message in messages]

    def get_all_chats(self, user_id: str) -> List[Dict[str, str]]:
        pattern = f"chat:{user_id}:*:meta"
        keys = self.client.keys(pattern)
        chats: List[Dict[str, str]] = []
        prefix = f"chat:{user_id}:"
        suffix = ":meta"
        for key in keys:
            # Extract chat_id from "chat:{user_id}:{chat_id}:meta"
            remainder = key[len(prefix):]  # "{chat_id}:meta"
            chat_id = remainder[:-len(suffix)]  # Remove ":meta" suffix
            chat_name = self.get_chat_metadata(user_id, chat_id)
            chats.append({"chat_id": chat_id, "chat_name": chat_name})
        return chats

    def create_chat(self, user_id: str, chat_id: str, chat_name: str) -> Dict[str, str]:
        meta_key = f"chat:{user_id}:{chat_id}:meta"
        self.client.hset(meta_key, mapping={"chat_name": chat_name, "created_at": str(time.time())})
        self.client.expire(meta_key, self.ttl)
        return {"chat_id": chat_id, "chat_name": chat_name}

    def delete_chat(self, user_id: str, chat_id: str) -> bool:
        chat_key = f"chat:{user_id}:{chat_id}"
        meta_key = f"chat:{user_id}:{chat_id}:meta"
        deleted = self.client.delete(chat_key, meta_key)
        return deleted > 0

    def get_chat_metadata(self, user_id: str, chat_id: str) -> str:
        meta_key = f"chat:{user_id}:{chat_id}:meta"
        chat_name = self.client.hget(meta_key, "chat_name")
        return chat_name if chat_name else "Chat"

    def save_conn_id(self, user_id: str, chat_id: str, conn_id: str) -> bool:
        conn_id_key = f"chat:{user_id}:{chat_id}:conn_id"
        self.client.set(conn_id_key, conn_id)
        self.client.expire(conn_id_key, self.ttl)
        return True

    def get_conn_id(self, user_id: str, chat_id: str) -> Optional[str]:
        conn_id_key = f"chat:{user_id}:{chat_id}:conn_id"
        return self.client.get(conn_id_key)


chat_cache = ChatCache()



