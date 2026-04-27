# caesar.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .caesar <сдвиг> <текст>': ' .caesar <сдвиг> <текст>', 'lang_code': 'lang_code', '❌ .caesar <сдвиг> <текст>': '❌ .caesar <сдвиг> <текст>', '🔐 Цезарь ({shift}): `{result}`': '🔐 Цезарь ({shift}): `{result}`', 'Команда caesar': 'Команда caesar', 'Command caesar': 'Command caesar'}

# caesar.py
#Ru: Команда caesar
#En: Command caesar
#Ua: Команда caesar

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .caesar <сдвиг> <текст>': ' .caesar <сдвиг> <текст>'},
    "en": {' .caesar <сдвиг> <текст>': ' .caesar <сдвиг> <текст>'},
    "ua": {' .caesar <сдвиг> <текст>': ' .caesar <сдвиг> <текст>'}
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
        return texts["❌ .caesar <сдвиг> <текст>"]
    try:
        shift = int(args[0])
        text = " ".join(args[1:])
        result = "".join(chr((ord(c)-97+shift)%26+97) if c.islower() else chr((ord(c)-65+shift)%26+65) if c.isupper() else c for c in text)
        return ftexts["🔐 Цезарь ({shift}): `{result}`"]
    except:
        return texts["❌ .caesar <сдвиг> <текст>"]



async def get_description():
    return {
        "ru": texts["Команда caesar"],
        "en": texts["Command caesar"],
        "ua": texts["Команда caesar"]
    }
