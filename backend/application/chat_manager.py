import uuid
from typing import Any, Dict, List, Optional

from domain.ports.chat_cache_port import ChatCachePort

from application.connection_manager import ConnectionManager


class ChatManager:
    def __init__(self, chat_cache_port: ChatCachePort, connection_manager: ConnectionManager):
        self.chat_cache = chat_cache_port
        self.connection_manager = connection_manager

    def list_user_chats(self, user_id: str) -> List[Dict[str, str]]:
        return self.chat_cache.get_all_chats(user_id)

    def create_chat(self, user_id: str, chat_name: Optional[str], db_type: str, connection_params: dict) -> Dict[str, str]:
        chat_id = str(uuid.uuid4())
        name = chat_name or "New Chat"

        # Create chat first
        chat_summary = self.chat_cache.create_chat(user_id, chat_id, name)

        try:
            # Establish connection
            conn_id = self.connection_manager.create_connection(db_type, connection_params)
            self.save_connection_id(user_id, chat_id, conn_id)
            return chat_summary
        except Exception:
            # rollback chat if connection fails
            self.delete_chat(user_id, chat_id)
            raise

    def get_chat(self, user_id: str, chat_id: str) -> Optional[Dict[str, Any]]:
        messages = self.chat_cache.get_chat_history(user_id, chat_id)
        if messages is None:
            return None
        chat_name = self.chat_cache.get_chat_metadata(user_id, chat_id)
        return {
            "chatId": chat_id,
            "chatName": chat_name,
            "queryResponses": messages,
        }

    def delete_chat(self, user_id: str, chat_id: str) -> bool:
        return self.chat_cache.delete_chat(user_id, chat_id)

    def save_connection_id(self, user_id: str, chat_id: str, conn_id: str) -> bool:
        return self.chat_cache.save_conn_id(user_id, chat_id, conn_id)

    def get_connection_id(self, user_id: str, chat_id: str) -> Optional[str]:
        return self.chat_cache.get_conn_id(user_id, chat_id)

    def add_chat_block(self, user_id: str, chat_id: str, message: Any) -> None:
        self.chat_cache.add_chat_block(user_id, chat_id, message)

