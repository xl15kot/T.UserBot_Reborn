# spam.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .spam <кол-во> <текст>': ' .spam <кол-во> <текст>', 'lang_code': 'lang_code', '❌ .spam <кол-во> <текст>': '❌ .spam <кол-во> <текст>', '{text}': '{text}', 'Команда spam': 'Команда spam', 'Command spam': 'Command spam'}

# spam.py
#Ru: Команда spam
#En: Command spam
#Ua: Команда spam

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .spam <кол-во> <текст>': ' .spam <кол-во> <текст>'},
    "en": {' .spam <кол-во> <текст>': ' .spam <кол-во> <текст>'},
    "ua": {' .spam <кол-во> <текст>': ' .spam <кол-во> <текст>'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if len(args) < 2:
        return texts["❌ .spam <кол-во> <текст>"]
    try:
        n = min(int(args[0]), 50)
        text = " ".join(args[1:])
        await event.delete()
        for i in range(n):
            await event.respond(ftexts["{text}"])
            await asyncio.sleep(0.35)
        return None
    except:
        return texts["❌ .spam <кол-во> <текст>"]



async def get_description():
    return {
        "ru": texts["Команда spam"],
        "en": texts["Command spam"],
        "ua": texts["Команда spam"]
    }
