# rot13.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .rot13 <текст>': ' .rot13 <текст>', 'lang_code': 'lang_code', '❌ .rot13 <текст>': '❌ .rot13 <текст>', '🔐 ROT13: `{result}`': '🔐 ROT13: `{result}`', 'Команда rot13': 'Команда rot13', 'Command rot13': 'Command rot13'}

# rot13.py
#Ru: Команда rot13
#En: Command rot13
#Ua: Команда rot13

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .rot13 <текст>': ' .rot13 <текст>'},
    "en": {' .rot13 <текст>': ' .rot13 <текст>'},
    "ua": {' .rot13 <текст>': ' .rot13 <текст>'}
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
        return texts["❌ .rot13 <текст>"]
    text = " ".join(args)
    result = "".join(chr((ord(c)-97+13)%26+97) if c.islower() else chr((ord(c)-65+13)%26+65) if c.isupper() else c for c in text)
    return ftexts["🔐 ROT13: `{result}`"]



async def get_description():
    return {
        "ru": texts["Команда rot13"],
        "en": texts["Command rot13"],
        "ua": texts["Команда rot13"]
    }
