import json
from core.brain.realtime_ai import RealtimeAI
from core.brain.groq_service import GroqService
from core.brain.chat_service import ChatService
from core.brain.prompt import get_aether_system_prompt
from core.brain.decision_making_model import DecisionMakingModel
from core.utils.time_info import get_time_information


class BrainService:
    """
    Aether's Brain Service — orchestrates all input processing.

    Pipeline:
      1. DecisionMakingModel (DMM) classifies the query → 'general' or 'realtime'
      2. If 'realtime': fetch live data via RealtimeAI, inject into context
      3. Generate final response via Groq (main LLM)
    """

    def __init__(self):
        self.realtime_ai = RealtimeAI()
        self.groq_service = GroqService()
        self.chat_service = ChatService(get_aether_system_prompt())
        self.dmm = DecisionMakingModel()

    def process_input(self, user_input: str, chat_history: list = None) -> str:
        """
        Main processing pipeline with DMM-gated real-time search.
        """
        try:
            current_time_context = get_time_information()

            # ── Stage 1: DMM Classification ──────────────────────────────
            decision = self.dmm.classify(user_input)

            # ── Stage 2: Fetch realtime data if needed ────────────────────
            realtime_context = ""
            if decision == "realtime":
                print(f"\n  ⚡ [DMM] Decision: realtime → Searching web...")
                search_result = self.realtime_ai.search(user_input)
                if search_result and not search_result.startswith("Error"):
                    realtime_context = f"\n\n[LIVE WEB SEARCH RESULT]\n{search_result}"
                else:
                    print(f"  ⚠ Search returned: {search_result}")
            else:
                print(f"\n  ✓ [DMM] Decision: general → Answering from knowledge")

            # ── Stage 3: Build messages with all context ──────────────────
            additional_context = current_time_context + realtime_context

            messages = self.chat_service.build_messages(
                user_input, chat_history, additional_context=additional_context
            )

            # ── Stage 4: Generate final response ──────────────────────────
            response_message = self.groq_service.generate_response(messages)
            return response_message.content

        except Exception as e:
            print(f"\n[AETHER ERROR] Brain processing failed: {e}")
            return "I encountered an error processing your request. Please check my diagnostic logs."
