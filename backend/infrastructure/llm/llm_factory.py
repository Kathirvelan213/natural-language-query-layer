import os
from .groqLLM import GroqLLM
from domain.ports.llm_port import LLMPort

def get_llm()->LLMPort:
    provider = os.getenv("LLM_PROVIDER", "openai")

    if provider == "groq":
        return GroqLLM()
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {provider}")
