# leet.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .leet <текст>': ' .leet <текст>', 'lang_code': 'lang_code', '❌ .leet <текст>': '❌ .leet <текст>', '🔥 `{result}`': '🔥 `{result}`', 'Команда leet': 'Команда leet', 'Command leet': 'Command leet'}

# leet.py
#Ru: Команда leet
#En: Command leet
#Ua: Команда leet

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .leet <текст>': ' .leet <текст>'},
    "en": {' .leet <текст>': ' .leet <текст>'},
    "ua": {' .leet <текст>': ' .leet <текст>'}
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
        return texts["❌ .leet <текст>"]
    lm = {"a":"4","e":"3","i":"1","o":"0","t":"7","s":"5"}
    text = " ".join(args)
    result = "".join(lm.get(c.lower(), c) for c in text)
    return ftexts["🔥 `{result}`"]



async def get_description():
    return {
        "ru": texts["Команда leet"],
        "en": texts["Command leet"],
        "ua": texts["Команда leet"]
    }
