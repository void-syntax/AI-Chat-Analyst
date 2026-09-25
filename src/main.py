import argparse
import ollama
from pathlib import Path
from model_prompts import mode_prompts, system_prompt

parser = argparse.ArgumentParser()

parser.add_argument("--chat", help="Path to chat export file", required=True)
parser.add_argument("--model", help="Model to use for analysis", default="qwen3.5:9b")
parser.add_argument("--mode", help="Analysis mode", choices=list(mode_prompts.keys()), default="Default")

args = parser.parse_args()

chat_path = Path(args.chat)

if not chat_path.is_file():
    parser.error(f"Chat file does not exist: {chat_path}")

chat = chat_path.read_text(encoding="utf-8")

prompt = f"""
{mode_prompts[args.mode]}

<chat>
{chat}
</chat>
"""

response = ollama.chat(
    model=args.model,
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": prompt,
        },
    ],
    stream=True,
    think=False,
    options={
        "num_ctx": 8192,
        "temperature": 0.2,
    },
)

for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)

print()