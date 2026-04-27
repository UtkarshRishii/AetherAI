import os
import json
import uuid
from datetime import datetime
from config import Config
import chromadb
from chromadb.config import Settings

class MemoryManager:
    def __init__(self, session_id: str = "default_session"):
        self.session_id = session_id
        self.history_file = os.path.join(Config.HISTORY_DIR, f"{self.session_id}.json")
        self.max_context_messages = 20 # Keep last 20 messages for active context
        self.chat_history = self._load_history()
        
        # Initialize ChromaDB for Long-Term Memory
        try:
            self.chroma_client = chromadb.PersistentClient(path=Config.VECTOR_DB_DIR)
            self.collection = self.chroma_client.get_or_create_collection(name="aether_memory")
            self.chroma_available = True
        except Exception as e:
            print(f"[AETHER WARNING] Vector DB initialization failed: {e}")
            self.chroma_available = False

    def _load_history(self) -> list:
        """Loads chat history from the JSON file."""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not decode {self.history_file}. Starting fresh.")
                return []
        return []

    def _save_history(self):
        """Saves current chat history to the JSON file."""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.chat_history, f, indent=4)
        except Exception as e:
            print(f"Error saving memory: {e}")

    def add_message(self, role: str, content: str):
        """Adds a message to the memory and saves it."""
        timestamp = datetime.now().isoformat()
        message = {
            "role": role,
            "content": content,
            "timestamp": timestamp
        }
        self.chat_history.append(message)
        self._save_history()
        
        if self.chroma_available:
            try:
                doc_id = str(uuid.uuid4())
                self.collection.add(
                    documents=[content],
                    metadatas=[{"role": role, "session_id": self.session_id, "timestamp": timestamp}],
                    ids=[doc_id]
                )
            except Exception as e:
                print(f"[AETHER WARNING] Failed to save memory to Vector DB: {e}")

    def get_context(self, current_input: str = None) -> list:
        """Returns the most recent messages for LLM context window + relevant long term memories."""
        context = []
        
        # 1. Retrieve relevant long-term memories if input is provided
        if self.chroma_available and current_input:
            try:
                results = self.collection.query(
                    query_texts=[current_input],
                    n_results=5
                )
                
                if results and results['documents'] and len(results['documents'][0]) > 0:
                    long_term_memory = "Recall these relevant past memories from previous interactions (treat as absolute context):\n"
                    added_memory = False
                    for i, doc in enumerate(results['documents'][0]):
                        # Avoid adding the exact same string we just typed
                        if doc.strip().lower() == current_input.strip().lower():
                            continue
                            
                        metadata = results['metadatas'][0][i]
                        role = metadata.get("role", "unknown")
                        time_str = metadata.get("timestamp", "unknown time")
                        
                        # Format timestamp to be more readable
                        try:
                            dt = datetime.fromisoformat(time_str)
                            time_str = dt.strftime("%Y-%m-%d %H:%M")
                        except:
                            pass
                            
                        long_term_memory += f"- [{time_str}] {role.capitalize()} said: {doc}\n"
                        added_memory = True
                    
                    if added_memory:
                        context.append({"role": "system", "content": long_term_memory})
            except Exception as e:
                print(f"[AETHER WARNING] Memory retrieval failed: {e}")
                
        # 2. Add recent messages
        recent_messages = self.chat_history[-self.max_context_messages:]
        for msg in recent_messages:
            context.append({"role": msg["role"], "content": msg["content"]})
            
        return context

    def clear_memory(self):
        """Clears the current session memory (short term). Vector DB remains."""
        self.chat_history = []
        self._save_history()
