import json
import time
import os
from dotenv import load_dotenv
from .redis_client import redis_client
from models.nlQuery import NLQueryResponse

load_dotenv()
CHAT_TTL = int(os.getenv("CHAT_TTL", "86400"))

def add_chat_block(user_id: str, chat_id: str, message:NLQueryResponse):
    key = f"chat:{user_id}:{chat_id}"

    redis_client.rpush(key, message.model_dump_json())

    # set TTL only if not already set
    redis_client.expire(key, CHAT_TTL)
        
        
def get_chat_history(user_id: str, chat_id: str):
    key = f"chat:{user_id}:{chat_id}"

    # Check if chat exists
    if not redis_client.exists(key):
        return None
    
    messages = redis_client.lrange(key, 0, -1)
    return [json.loads(m) for m in messages]


def get_all_chats(user_id: str):
    """Get all chat IDs for a user with their metadata"""
    pattern = f"chat:{user_id}:*"
    keys = redis_client.keys(pattern)
    
    chats = []
    for key in keys:
        # Skip metadata keys
        if key.endswith(":meta"):
            continue
            
        # Extract chat_id from key (format: chat:user_id:chat_id)
        chat_id = key.split(":")[-1]
        
        # Get chat name using the metadata function
        chat_name = get_chat_metadata(user_id, chat_id)
        
        chats.append({
            "chat_id": chat_id,
            "chat_name": chat_name
        })
    print(chats)
    
    return chats


def create_chat(user_id: str, chat_id: str, chat_name: str):
    """Create a new chat with metadata"""
    meta_key = f"chat:{user_id}:{chat_id}:meta"
    
    redis_client.hset(meta_key, mapping={
        "chat_name": chat_name,
        "created_at": str(time.time())
    })
    redis_client.expire(meta_key, CHAT_TTL)
    
    return {
        "chat_id": chat_id,
        "chat_name": chat_name
    }


def delete_chat(user_id: str, chat_id: str):
    """Delete a chat and its metadata"""
    key = f"chat:{user_id}:{chat_id}"
    meta_key = f"{key}:meta"
    
    # Delete both the chat messages and metadata
    deleted = redis_client.delete(key, meta_key)
    
    return deleted > 0


def get_chat_metadata(user_id: str, chat_id: str):
    """Get metadata for a specific chat"""
    meta_key = f"chat:{user_id}:{chat_id}:meta"
    chat_name = redis_client.hget(meta_key, "chat_name")
    return chat_name if chat_name else "Chat"



