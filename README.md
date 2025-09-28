# Amber — Your new wife. Live with it now =D

Amber is a lightweight local chat companion that uses the [OpenAI Responses API](https://platform.openai.com/docs/guides/text-generation) for conversation.  
It’s designed to be **short, witty, sarcastic, and fun** — more like a real friend than a corporate assistant.

> ⚡️ Built and tested on Arch Linux, but works anywhere with Python 3.10+.

---

## ✨ Features

- 💬 **Conversational memory** — keeps recent chat history locally (JSONL file).
- 🧠 **Custom personality** — defined in `modules.py` & `SYSTEM_PROMPT`.
- ⏱️ **Time-aware** — automatically knows current date/time for more natural replies.
- 🧩 **Modular design** — easy to add custom functions or “tools” the AI can call.
- 🔒 **Runs locally** — only calls OpenAI’s API, no extra services.

---

## !!!ATENTION!!!

You have to create and use your own API. I don't want to pay after you =D
It's not to expensive, but anyway --> https://platform.openai.com/

---

## 🛠️ Installation

### Clone repository

```bash
git clone https://github.com/babaikka/AI-Wife.git
cd AI_Wife

### For normal peoples

```bash
pip install -r requirements.txt

### For real Arch btw femboys

```bash
sudo pacman -S python-openai

### Add API to your .bashrc / .zshrc / .fuckrc whatever

```bash
echo 'export OPENAI_API_KEY=<YOUR API CODE RIGHT HIRE>' >> ~/.fuckrc


### Talk with your new wife

```bash
chmod +x app.py
./app.py

