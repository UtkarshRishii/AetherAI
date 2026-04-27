# Aether

![Aether Banner](https://via.placeholder.com/800x200/00FFFF/000000?text=AETHER)

*Advanced Entity for Thinking, Heuristics, and Empirical Reasoning*

A sophisticated AI assistant designed for intelligent conversations, equipped with voice capabilities, long-term memory retention, and advanced reasoning powered by cutting-edge AI models. Created by Utkarsh Rishi.

## Features

- **Conversational AI**: Powered by Groq's LLaMA 3.3 70B model for highly logical and coherent responses
- **Voice Interaction**: Integrated Text-to-Speech (TTS) using Microsoft Edge TTS for audible responses
- **Persistent Memory**: Long-term memory storage using Chroma vector database for context-aware conversations
- **Rich CLI Interface**: Beautiful, colorful terminal interface with Rich library for enhanced user experience
- **Session Management**: Unique session IDs with memory clearing capabilities
- **Web Search Integration**: DuckDuckGo search functionality for real-time information retrieval
- **Markdown Support**: Responses rendered with proper markdown formatting

## Prerequisites

- Python 3.8 or higher
- A Groq API key (obtain from [groq.com](https://groq.com))

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Aether
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Run the AI assistant:

```bash
python run_aether.py
```

### Interaction

- Type your messages in the prompt: `⟩ You`
- The AI will respond both textually (with rich formatting) and audibly
- Use special commands:
  - `exit` or `quit`: Shutdown the assistant
  - `clear`: Wipe current session memory

### Configuration

You can modify settings in `config.py`:
- Model selection (default: llama-3.3-70b-versatile)
- Temperature settings
- Token limits

## Architecture

```
Aether/
├── core/
│   ├── main.py              # Main application entry point
│   ├── brain/               # AI processing modules
│   │   ├── brain_service.py # Core brain logic
│   │   ├── groq_service.py  # Groq API integration
│   │   ├── chat_service.py  # Chat processing
│   │   └── prompt.py        # System prompts
│   ├── memory/              # Memory management
│   │   └── memory_manager.py # Vector database operations
│   ├── services/            # External services
│   │   └── tts.py           # Text-to-speech engine
│   └── utils/               # Utility functions
├── database/                # Persistent data storage
│   ├── vector_store/        # Chroma vector database
│   ├── aether_history/      # Session history
│   └── learning_data/       # Learning data
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
└── run_aether.py            # Application launcher
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

### Social Media
- **Business Email**: workwithmrrishi@email.com
- **Instagram**: [utkarshrishhi](http://instagram.com/utkarshrishhi)
- **Falcon Instagram**: [heyfalcon.ai](http://instagram.com/heyfalcon.ai)
- **Telegram Channel**: [ArcDevsOG](https://t.me/ArcDevsOG)
- **Telegram Group**: [ArcAgents](https://t.me/ArcAgents)
- **Falcon Website**: [heyfalconai.in](https://www.heyfalconai.in/)
- **WhatsApp Channel**: [Join Here](https://whatsapp.com/channel/0029Vb792mHInlqWSB6k6f38)</content>

**Created by Utkarsh Rishi**
