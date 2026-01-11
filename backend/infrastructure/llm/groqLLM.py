# services/llm/groq.py
import os
from groq import Groq
from domain.ports.llm_port import LLMPort

class GroqLLM(LLMPort):
    def __init__(
        self,
        model: str = "llama-3.3-70b-versatile",
        temperature: float = 0.7,
        max_tokens: int = 1024,
        top_p: float = 1.0,
    ):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY not set")

        self.client = Groq(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p

    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_completion_tokens=self.max_tokens,
            top_p=self.top_p,
            stream=False,
        )
        return completion.choices[0].message.content
