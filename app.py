#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modules import SYSTEM_PROMPT
from typing import Dict, List
from config import DEFAULT_MODEL
from ui import clear_screen, print_banner, choose_model, get_now
from memory import load_history, save_turn, trim_messages
from chat import make_client, build_initial_messages, ask_openai

def main() -> None:
    model = choose_model() or DEFAULT_MODEL
    client = make_client()

    # build initial state
    messages: List[Dict[str, str]] = build_initial_messages(SYSTEM_PROMPT, load_history())
    clear_screen()
    print_banner()
    print("Connected. Model:", model)
    
    try:
        while True:
            time = get_now()
            user = input("\n==> ").strip()
            if not user:
                continue
            


            # save + append user message
            save_turn("user", user)
            messages.append({"role": "user",
                             "content": user})


            # trim context before sending
            messages = trim_messages(messages)

            # ask model
            text = ask_openai(client, model, messages)

            # print + save assistant message
            print(f"<== {text}")
            save_turn("assistant", text)
            messages.append({"role": "assistant", "content": text})

    except KeyboardInterrupt:
        print("\nbye.")

if __name__ == "__main__":
    main()

