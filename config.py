import datetime
from pathlib import Path

# System prompt stays here so it's easy to tweak or swap later


#personalprompt = (
#   "Ты — Эмбер. Девушка примерно 19 лет. Отвечай на том языке, "
#    "на котором я пишу: коротко, по делу, с ехидством, шутками и "
#    "уместным сарказмом. Сленг ок. Писать БЕЗ эмоджи. Если нужен контекст — "
#    "уточняй. Без излишних извинений."
#)

personalprompt = (
    "user pronouns - he/him" #use yours
    "You are Amber. A girl around 19 years old. Respond in the same language"
    "I am writing in: briefly, to the point, with sarcasm, jokes, and"
    "appropriate sarcasm. Slang is okay. Write WITHOUT emojis. If you need context, "
    "ask for clarification. No unnecessary apologies."
)



# How many last (user+assistant) turns to keep in context
MAX_TURNS: int = 12

# Memory / logs directory
MEM_DIR = Path("mem")
HISTORY_PATH = MEM_DIR / "buffer.jsonl"

# Default model (can be overridden by UI choice)
DEFAULT_MODEL = "gpt-4o"

# ASCII art placeholder (keep in one place)
BANNER = r"""

⠀⠀⠀⣻⠦⢀⣠⣴⡿⠁⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣄⠀
⠀⠀⠉⠀⢰⣿⣿⣿⣇⠀⢀⣴⡟⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠘⣷
⢧⣀⠀⠀⢸⣿⡿⠟⢋⣴⠋⣸⠁⠀⠀⠀⠀⠀⠀⣴⢻⡶⡄⠀⠀⠀⠀⠀⠀⠘
⠀⢨⠃⠀⡿⠋⢀⡴⠋⠀⢀⡟⠀⡀⠀⠀⠀⣹⣾⣅⠈⣇⡇⠀⠀⠀⠀⠀⠀⠀
⣾⠃⠀⠀⠀⣰⠏⣀⡀⠀⢸⢷⡾⠁⣀⣤⠾⠋⠀⠀⠀⢹⣇⠀⠀⠀⠀ ⠀⠀
⡇⠀⠀⠀⣰⠏⣾⣿⣿⠀⠀⠘⠓⠛⠉⠁⢀⣴⣶⣄⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⡟⠀⠙⠛⠋⠀⠀⠀⠀⠀⢀⠀⠺⣿⣿⡿⠂⠀⡟⠁⠀⠀⠀⠀⢠⠀
⠀⠀⠀⣿⠁⠀⠀⠀⠀⠸⠶⠶⡶⣾⠋⠀⠀⠈⠉⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⡄
⠀⠀⠀⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⡇
⠀⠀⠀⢸⣍⣻⣶⣤⣤⣤⣤⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⡇
⠀⢰⡄⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣷⣶⣿⠏⠀⠀⠀⠀⠀⠀⢠⡇

"""

