class ChatService:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def build_messages(
        self, user_input: str, chat_history: list = None, additional_context: str = ""
    ) -> list:
        """
        Builds the messages list for the LLM API call.
        """
        messages = [{"role": "system", "content": self.system_prompt}]

        # Add conversation history
        if chat_history:
            for msg in chat_history:
                messages.append({"role": msg["role"], "content": msg["content"]})

        # Add current user input with any additional context
        full_user_input = user_input
        if additional_context:
            full_user_input += f"\n\n[SYSTEM CONTEXT INJECTED (DO NOT READ OUT LOUD)]\n{additional_context}"
        messages.append({"role": "user", "content": full_user_input})

        return messages
