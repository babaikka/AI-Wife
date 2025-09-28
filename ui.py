import json
import os
import datetime

from pathlib import Path
from typing import Dict, List
from config import MEM_DIR, HISTORY_PATH, MAX_TURNS, BANNER

def choose_model():
    while True:
        os.system("clear") 
        print_banner()
        print("Chose model: \n1 - gpt-4o-mini \n2 - gpt-4o\n")
        modelchose = str(input("==> "))

        if modelchose == '1':
            MODEL = "gpt-4o-mini"
            break

        elif modelchose == '2':
            MODEL = "gpt-4o"
            break

def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_banner():
    print(BANNER)

def ensure_mem_dir() -> None:
    MEM_DIR.mkdir(exist_ok=True)

def clear_screen():
    os.system("clear")

def load_history() -> List[Dict[str, str]]:
    """
    Read chat history (jsonl). Only 'user' and 'assistant' roles are kept.
    """
    ensure_mem_dir()
    if not HISTORY_PATH.exists():
        return []
    items: List[Dict[str, str]] = []
    with HISTORY_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
                if msg.get("role") in {"user", "assistant"} and "content" in msg:
                    items.append({"role": msg["role"], "content": msg["content"]})
            except json.JSONDecodeError:
                # skip broken lines silently
                continue
    return items

def save_turn(role: str, content: str) -> None:
    """
    Append a single message to history jsonl.
    """
    ensure_mem_dir()
    rec = {"role": role, "content": content}
    with HISTORY_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def trim_messages(messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Keep system message at index 0; trim the rest to the last MAX_TURNS items.
    """
    if not messages:
        return messages
    sysmsg = messages[0]
    rest = messages[1:]
    trimmed_rest = rest[-MAX_TURNS:]
    return [sysmsg] + trimmed_rest

