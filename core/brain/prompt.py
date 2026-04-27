import os
from config import Config

def get_aether_system_prompt() -> str:
    """
    Dynamically constructs the system prompt by combining the base persona
    with any customized assistant directives and user profile data stored
    in the learning_data directory.
    """
    base_prompt = (
        "You are AETHER (Advanced Entity for Thinking, Heuristics, and Empirical Reasoning), "
        "an extremely advanced, logical, and highly capable AI assistant created by \"Utkarsh Rishi\"."
    )
    
    # Load assistant data
    assistant_data_path = os.path.join(Config.LEARNING_DIR, "assistant_data.txt")
    assistant_data = ""
    if os.path.exists(assistant_data_path):
        try:
            with open(assistant_data_path, "r", encoding="utf-8") as f:
                assistant_data = f.read().strip()
        except Exception as e:
            print(f"[AETHER WARNING] Could not read assistant_data.txt: {e}")
            
    # Load user data
    user_data_path = os.path.join(Config.LEARNING_DIR, "user_data.txt")
    user_data = ""
    if os.path.exists(user_data_path):
        try:
            with open(user_data_path, "r", encoding="utf-8") as f:
                user_data = f.read().strip()
        except Exception as e:
            print(f"[AETHER WARNING] Could not read user_data.txt: {e}")

    final_prompt = base_prompt + "\n\n"
    if assistant_data:
        final_prompt += f"--- ASSISTANT DIRECTIVES & SYSTEM PROMPT ---\n{assistant_data}\n\n"
    if user_data:
        final_prompt += f"--- USER PROFILE & DETAILS ---\n{user_data}\n\n"
        
    return final_prompt