from groq import Groq
from config import Config

_DMM_SYSTEM_PROMPT = """\
You are a query classifier. Output EXACTLY one word: "general" or "realtime".

CATEGORIES:

general — Conversational, chitchat, knowledge questions answerable from memory or \
general knowledge. No tools or internet needed.
Examples: "Tell me a joke", "Explain recursion", "Write me a poem", "How does gravity work?", \
"What is Python?", "Thanks for that", "You're awesome", "Remember my chat ID is 123", \
"Hello", "Hi", "How are you?", "What is your name?", "What can you do?", \
"Explain machine learning", "What is quantum physics?", "Write me code for X"

realtime — Questions that need LIVE WEB SEARCH for current, time-sensitive, or factual \
information about real people, events, places, or the world.
Examples: "Who is Elon Musk?", "What's the weather today?", "Latest AI news", \
"Tesla stock price", "Who won the IPL match?", "What happened in Ukraine?", \
"How old is MS Dhoni?", "Best restaurants near me", "Latest news", \
"What happened today?", "Current bitcoin price", "Who won the election?"

RULE: Questions about real people, current events, recent facts → ALWAYS "realtime".

RULES:
- If the user is asking about a real person, place, or current event → "realtime"
- If the user is chatting, asking general knowledge questions, or sharing info → "general"
- When someone shares personal info like "my favorite color is blue" → "general"
- Simple greetings, thank you, goodbye → "general"
- Coding questions, math, science concepts → "general"
- Anything requiring live data or internet → "realtime"

Output ONLY the single word. No explanation. No punctuation.\
"""


class DecisionMakingModel:
    """
    A lightweight Groq-powered query classifier.
    Routes each user query to the correct processing pipeline:
      - 'general' → Answer directly from LLM knowledge
      - 'realtime' → Trigger web search before answering
    Uses a fast model (llama-3.1-8b-instant) to minimize latency.
    """

    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        # Use the fastest available model for low-latency classification
        self.model = "llama-3.1-8b-instant"

    def classify(self, user_input: str) -> str:
        """
        Classifies the user input and returns 'general' or 'realtime'.
        Defaults to 'general' on any failure to avoid unnecessary searches.
        """
        if not user_input or not user_input.strip():
            return "general"

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": _DMM_SYSTEM_PROMPT},
                    {"role": "user", "content": user_input.strip()},
                ],
                temperature=0.0,   # Zero temperature — deterministic classification
                max_tokens=5,      # Only need one word
            )
            decision = completion.choices[0].message.content.strip().lower()

            # Sanitize output — only accept known categories
            if decision in ("realtime", "general"):
                return decision

            # If the model returned something unexpected, default to general
            return "general"

        except Exception as e:
            print(f"[DMM WARNING] Classification failed: {e}. Defaulting to 'general'.")
            return "general"