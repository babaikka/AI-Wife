import os
import sys
from typing import Dict, List
from openai import OpenAI

def ensure_api_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: set OPENAI_API_KEY env var first.", file=sys.stderr)
        sys.exit(1)

def make_client() -> OpenAI:
    ensure_api_key()
    return OpenAI()

def build_initial_messages(system_prompt: str, history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    messages: List[Dict[str, str]] = [{"role": "system",
                                       "content": system_prompt}]
    messages += history
    return messages

def ask_openai(client: OpenAI, model: str, messages: List[Dict[str, str]]) -> str:
    """
    Call Responses API and return plain text.
    """
    resp = client.responses.create(
        model=model,
        input=messages
    )
    # Be defensive in case of different SDK structures in the future
    try:
        return resp.output[0].content[0].text.strip()
    except Exception:
        # fallback: stringify
        return str(resp)

