import datetime
from config import personalprompt

def get_now():
    time = 'сейчас ', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time

def get_personal():
    personal = personalprompt
    return personal

def send_modules():
    systemprompt = f"{get_personal()} {get_now()}"

    return systemprompt

SYSTEM_PROMPT = send_modules()
