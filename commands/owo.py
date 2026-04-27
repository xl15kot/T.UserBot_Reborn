# owo.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .owo <текст>': ' .owo <текст>', 'lang_code': 'lang_code', '❌ .owo <текст>': '❌ .owo <текст>', '{text} {random.choice([uwu,owo,(◕ᴗ◕✿)])}': '{text} {random.choice([uwu,owo,(◕ᴗ◕✿)])}', 'Команда owo': 'Команда owo', 'Command owo': 'Command owo'}

# owo.py
#Ru: Команда owo
#En: Command owo
#Ua: Команда owo

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .owo <текст>': ' .owo <текст>'},
    "en": {' .owo <текст>': ' .owo <текст>'},
    "ua": {' .owo <текст>': ' .owo <текст>'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if not args:
        return texts["❌ .owo <текст>"]
    text = " ".join(args)
    for fr,to in [("r","w"),("l","w")]:
        text = text.replace(fr, to)
    return f"{text} {random.choice(['uwu','owo','(◕ᴗ◕✿)'])}"



async def get_description():
    return {
        "ru": texts["Команда owo"],
        "en": texts["Command owo"],
        "ua": texts["Команда owo"]
    }
