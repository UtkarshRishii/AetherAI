# Aether

> **A**dvanced **E**ntity for **T**hinking, **H**euristics & **E**mpirical **R**easoning

A sophisticated AI assistant built for intelligent conversations — with voice output, long-term vector memory, and web-connected reasoning powered by **LLaMA 3.3 70B** via Groq.

**Created by [Utkarsh Rishi](https://www.heyfalconai.in/)**

---

## Features

| Capability | Details |
|---|---|
| 🧠 **Conversational AI** | Groq-hosted LLaMA 3.3 70B — fast, logical, coherent responses |
| 🔊 **Voice output** | Microsoft Edge TTS renders every response as natural-sounding audio |
| 🗄️ **Persistent memory** | Chroma vector DB stores long-term context across sessions |
| 🔍 **Web search** | DuckDuckGo integration for real-time information retrieval |
| 🖥️ **Rich CLI** | Beautiful terminal UI via the Rich library with full markdown support |
| 🔐 **Session control** | Unique session IDs and instant memory-clear for fresh starts |

---

## Prerequisites

- **Python 3.8+** — verify with `python --version`
- **Groq API key** — obtain one at [groq.com](https://groq.com)

---

## Installation

**1. Clone the repository**
```bash
git clone <repository-url>
cd Aether
```

**2. Create a virtual environment** *(recommended)*
```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## Usage

```bash
python run_aether.py
```

Type your messages at the `⟩ You` prompt. Aether responds both in text and audio.

### Commands

| Command | Action |
|---|---|
| `exit` / `quit` | Gracefully shut down Aether |
| `clear` | Wipe the current session memory |

---

## Configuration

Edit `config.py` to tune Aether's behaviour:

| Setting | Default | Description |
|---|---|---|
| `model` | `llama-3.3-70b-versatile` | Groq model identifier |
| `temperature` | `0.7` | Sampling temperature |
| `max_tokens` | `4096` | Maximum tokens per response |

---

## Project Structure

```
Aether/
├── core/
│   ├── main.py                  # Application entry point
│   ├── brain/
│   │   ├── brain_service.py     # Core reasoning logic
│   │   ├── groq_service.py      # Groq API integration
│   │   ├── chat_service.py      # Message handling
│   │   └── prompt.py            # System prompts
│   ├── memory/
│   │   └── memory_manager.py    # Chroma vector DB operations
│   ├── services/
│   │   └── tts.py               # Text-to-speech engine
│   └── utils/                   # Shared utilities
├── database/
│   ├── vector_store/            # Chroma persistent storage
│   ├── aether_history/          # Per-session logs
│   └── learning_data/           # Accumulated learning data
├── config.py                    # All configuration constants
├── requirements.txt             # Python dependencies
└── run_aether.py                # Launcher script
```

---

## Contributing

Pull requests are welcome. Fork the repo, make your changes on a feature branch, and open a PR — all contributions are appreciated.

---

## License

Released under the [MIT License](LICENSE).

---

## Contact & Community

| Platform | Link |
|---|---|
| ✉️ Business email | [workwithmrrishi@email.com](mailto:workwithmrrishi@email.com) |
| 📸 Instagram | [@utkarshrishhi](https://instagram.com/utkarshrishhi) |
| 🦅 Falcon Instagram | [@heyfalcon.ai](https://instagram.com/heyfalcon.ai) |
| ✈️ Telegram channel | [ArcDevsOG](https://t.me/ArcDevsOG) |
| 👥 Telegram group | [ArcAgents](https://t.me/ArcAgents) |
| 🌐 Falcon website | [heyfalconai.in](https://www.heyfalconai.in/) |
| 💬 WhatsApp channel | [Join here](https://whatsapp.com/channel/0029Vb792mHInlqWSB6k6f38) |
