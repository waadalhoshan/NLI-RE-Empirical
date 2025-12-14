from __future__ import annotations
from dataclasses import dataclass
from tenacity import retry, stop_after_attempt, wait_exponential
import os

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

@dataclass
class OpenAISettings:
    model: str
    temperature: float = 0.0
    max_tokens: int = 256
    api_key_env: str = "OPENAI_API_KEY"

class ChatClient:
    def __init__(self, settings: OpenAISettings):
        if OpenAI is None:
            raise ImportError("openai package not installed; pip install -r requirements.txt")
        key = os.getenv(settings.api_key_env)
        if not key:
            raise EnvironmentError(f"Missing {settings.api_key_env}")
        self.client = OpenAI(api_key=key)
        self.settings = settings

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
    def chat(self, system_prompt: str, user_prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.settings.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self.settings.temperature,
            max_tokens=self.settings.max_tokens,
        )
        return resp.choices[0].message.content or ""
