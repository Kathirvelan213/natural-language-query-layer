import os
from .grokLLM import GroqLLM
from .geminiLLM import GeminiLLM

def get_llm():
    provider = os.getenv("LLM_PROVIDER", "openai")

    if provider == "groq":
        return GroqLLM()
    elif provider == "gemini":
        return GeminiLLM()
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {provider}")
