# AI Chat Analyst

An intelligent tool designed to parse, analyze, and summarize chat export histories using locally hosted Large Language Models via Ollama. Gain quick insights, extract key discussion topics, and analyze conversations without sending any sensitive data to third-party cloud services.

---

## 💡 How It Works

1. **Input Data**: You provide exported chat files (JSON, TXT, etc.).
2. **Local Inference**: Chat content is wrapped into configured prompts and passed directly to a local Ollama instance.
3. **Streaming Analysis**: Insights, topics, and summaries are streamed in real time to your console.

---

## ✨ Features

- **🔒 100% Privacy-Focused**: Runs completely offline via Ollama; no API keys or cloud services required.
- **🤖 Default Model**: Configured to use `qwen3.5:9b` out-of-the-box (`8k` context window, low temperature for deterministic output).
- **🎭 Analysis Modes**: Flexible analysis modes defined in `src/model_prompts.py`.
- **⚡ Streaming Output**: Real-time response streaming.

---

## 📋 Requirements

- **Python**: 3.10 or higher
- **Ollama**: Installed and running locally ([Ollama Official Site](https://ollama.com/))
- **Default Model**: `qwen3.5:9b` pulled via Ollama (`ollama pull qwen3.5:9b`)

---

## 🚀 Getting Started

### 1. Prerequisites Setup

Ensure Ollama is running and pull the default model:

```bash
# Verify Ollama installation
ollama --version

# Pull the default model
ollama pull qwen3.5:9b
```

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone [https://github.com/void-syntax/ai-chat-analyst.git](https://github.com/void-syntax/ai-chat-analyst.git)
cd AI-Chat-Analyst

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install ollama
```

### 3. Usage

Run the analysis script via `src/main.py`:

```bash
# Basic usage with default model & mode
python src/main.py --chat path/to/chat.txt

# Specify a custom model and analysis mode
python src/main.py --chat path/to/chat.txt --model llama3 --mode Default
```

#### CLI Arguments

| Argument | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `--chat` | **Yes** | — | Path to exported chat file |
| `--model` | No | `qwen3.5:9b` | Model name available in Ollama |
| `--mode` | No | `Default` | Analysis mode from `model_prompts.py` |

---

## 👥 Authors & Contributors

- **void-syntax** — Developer
- **[Engrise13](https://github.com/Engrise13)** — Developer

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
