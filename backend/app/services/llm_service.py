import ollama
from app.core.constants import DEFAULT_MODEL

class LLMService:

    def chat(self, prompt: str, system_prompt: str | None = None) -> str:

        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = ollama.chat(
            model=DEFAULT_MODEL,
            messages=messages
        )

        return response["message"]["content"]


llm_service = LLMService()