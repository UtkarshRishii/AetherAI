import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # Model Configuration
    # Using LLaMA 3 70B for advanced reasoning capabilities
    MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_DIR = os.path.join(BASE_DIR, "database")
    HISTORY_DIR = os.path.join(DATABASE_DIR, "aether_history")
    LEARNING_DIR = os.path.join(DATABASE_DIR, "learning_data")
    VECTOR_DB_DIR = os.path.join(DATABASE_DIR, "vector_store")
    
    # Ensure directories exist
    os.makedirs(HISTORY_DIR, exist_ok=True)
    os.makedirs(LEARNING_DIR, exist_ok=True)
    os.makedirs(VECTOR_DB_DIR, exist_ok=True)
    
    # AI Settings
    MAX_TOKENS = 2048
    TEMPERATURE = 0.5  # Keep it relatively low for "no delulu", highly logical responses
