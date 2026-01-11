"""Bootstrap initialization for dependency injection and singleton managers."""

from application.chat_manager import ChatManager
from application.query_orchestration import QueryManager
from application.connection_manager import ConnectionManager
from application.schema_manager import SchemaManager
from infrastructure.cache.chat_store import chat_cache
from infrastructure.llm.groqLLM import GroqLLM
from infrastructure.db_provider.db_provider_factory import DbProviderFactory


_schema_manager = SchemaManager()
_connection_manager = ConnectionManager(DbProviderFactory(), _schema_manager)

def get_connection_manager() -> ConnectionManager:
    """Get singleton ConnectionManager instance."""
    return _connection_manager

def get_schema_manager() -> SchemaManager:
    """Get singleton SchemaManager instance."""
    return _schema_manager

def get_chat_manager() -> ChatManager:
    """Get singleton ChatManager instance."""
    return ChatManager(chat_cache, _connection_manager)

def get_query_manager() -> QueryManager:
    """Get singleton QueryManager instance."""
    return QueryManager(GroqLLM(), _connection_manager, _schema_manager)
