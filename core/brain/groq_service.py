from groq import Groq
from config import Config


class GroqService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set in the environment or .env file.")

        self.client = Groq(api_key=self.api_key)
        self.model = Config.MODEL_NAME

    def generate_response(
        self, messages: list, tools: list = None, temperature: float = None, max_tokens: int = None
    ):
        """
        Generates a response from the Groq API using the provided messages.
        Supports tool calling if tools are provided.
        Returns the entire message object.
        """
        try:
            kwargs = {
                "messages": messages,
                "model": self.model,
                "temperature": temperature or Config.TEMPERATURE,
                "max_tokens": max_tokens or Config.MAX_TOKENS,
            }
            if tools:
                kwargs["tools"] = tools
                kwargs["tool_choice"] = "auto"
                
            chat_completion = self.client.chat.completions.create(**kwargs)
            return chat_completion.choices[0].message
        except Exception as e:
            raise Exception(f"Groq API error: {e}")
