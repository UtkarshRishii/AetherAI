# 🚀 Aether

<div align="center">

![Aether Banner](https://via.placeholder.com/800x200/00FFFF/000000?text=AETHER)

*Advanced Entity for Thinking, Heuristics, and Empirical Reasoning*

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-00FFFF)](https://groq.com)

**A sophisticated AI assistant with voice capabilities, long-term memory, and advanced reasoning. Created by [Utkarsh Rishi](mailto:workwithmrrishi@email.com)**

[📖 Documentation](#-usage) • [🔧 Installation](#-installation) • [🤝 Contributing](#-contributing)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **Conversational AI** | Powered by Groq's LLaMA 3.3 70B model for highly logical and coherent responses |
| 🎤 **Voice Interaction** | Integrated Text-to-Speech (TTS) using Microsoft Edge TTS for audible responses |
| 🧠 **Persistent Memory** | Long-term memory storage using Chroma vector database for context-aware conversations |
| 🎨 **Rich CLI Interface** | Beautiful, colorful terminal interface with Rich library for enhanced user experience |
| 🔄 **Session Management** | Unique session IDs with memory clearing capabilities |
| 🌐 **Web Search Integration** | DuckDuckGo search functionality for real-time information retrieval |
| 📝 **Markdown Support** | Responses rendered with proper markdown formatting |

## 📋 Prerequisites

- 🐍 Python 3.8 or higher
- 🔑 A Groq API key (obtain from [groq.com](https://groq.com))

## 🛠️ Installation

### Quick Start

1. **Clone the repository** 📥
   ```bash
   git clone <repository-url>
   cd Aether
   ```

2. **Create a virtual environment** (recommended) 🌐
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies** 📦
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** ⚙️

   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL_NAME=llama-3.3-70b-versatile
   ```

## 🚀 Usage

### Start the Assistant

```bash
python run_aether.py
```

### 💬 Interaction

- Type your messages in the prompt: `⟩ You`
- The AI will respond both **textually** (with rich formatting) and **audibly** 🎵
- Use special commands:
  - `exit` or `quit`: Shutdown the assistant ⏹️
  - `clear`: Wipe current session memory 🗑️

### ⚙️ Configuration

Customize settings in `config.py`:
- 🤖 Model selection (default: llama-3.3-70b-versatile)
- 🌡️ Temperature settings
- 📏 Token limits

## 🏗️ Architecture

```
Aether/
├── 🧠 core/
│   ├── main.py              # Main application entry point
│   ├── 🧠 brain/            # AI processing modules
│   │   ├── brain_service.py # Core brain logic
│   │   ├── groq_service.py  # Groq API integration
│   │   ├── chat_service.py  # Chat processing
│   │   └── prompt.py        # System prompts
│   ├── 💾 memory/           # Memory management
│   │   └── memory_manager.py # Vector database operations
│   ├── 🔧 services/         # External services
│   │   └── tts.py           # Text-to-speech engine
│   └── 🛠️ utils/            # Utility functions
├── 💾 database/             # Persistent data storage
│   ├── vector_store/        # Chroma vector database
│   ├── aether_history/      # Session history
│   └── learning_data/       # Learning data
├── ⚙️ config.py             # Configuration settings
├── 📦 requirements.txt      # Python dependencies
└── ▶️ run_aether.py          # Application launcher
```

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch: `git checkout -b feature/amazing-feature`
3. 💾 Commit your changes: `git commit -m 'Add amazing feature'`
4. 📤 Push to the branch: `git push origin feature/amazing-feature`
5. 🔄 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Created by Utkarsh Rishi** 👨‍💻

### 🌐 Social Media & Links

- 📧 **Business Email**: [workwithmrrishi@email.com](mailto:workwithmrrishi@email.com)
- 📸 **Instagram**: [@utkarshrishhi](http://instagram.com/utkarshrishhi)
- 🤖 **Falcon Instagram**: [@heyfalcon.ai](http://instagram.com/heyfalcon.ai)
- 📢 **Telegram Channel**: [@ArcDevsOG](https://t.me/ArcDevsOG)
- 💬 **Telegram Group**: [@ArcAgents](https://t.me/ArcAgents)
- 🌐 **Falcon Website**: [heyfalconai.in](https://www.heyfalconai.in/)
- 💬 **WhatsApp Channel**: [Join Here](https://whatsapp.com/channel/0029Vb792mHInlqWSB6k6f38)

---

<div align="center">

**Made with ❤️ by Utkarsh Rishi**

⭐ If you like this project, give it a star!

</div></content>
