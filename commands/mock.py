# mock.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .mock <текст>': ' .mock <текст>', 'lang_code': 'lang_code', '❌ .mock <текст>': '❌ .mock <текст>', 'Команда mock': 'Команда mock', 'Command mock': 'Command mock'}

# mock.py
#Ru: Команда mock
#En: Command mock
#Ua: Команда mock

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .mock <текст>': ' .mock <текст>'},
    "en": {' .mock <текст>': ' .mock <текст>'},
    "ua": {' .mock <текст>': ' .mock <текст>'}
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
        return texts["❌ .mock <текст>"]
    text = " ".join(args)
    return "".join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(text))



async def get_description():
    return {
        "ru": texts["Команда mock"],
        "en": texts["Command mock"],
        "ua": texts["Команда mock"]
    }
