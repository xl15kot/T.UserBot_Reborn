# pat.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .pat @user': ' .pat @user', 'lang_code': 'lang_code', '❌ .pat @user': '❌ .pat @user', '🖐 {args[0]}, тебя погладили по голове!': '🖐 {args[0]}, тебя погладили по голове!', 'Команда pat': 'Команда pat', 'Command pat': 'Command pat'}

# pat.py
#Ru: Команда pat
#En: Command pat
#Ua: Команда pat

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .pat @user': ' .pat @user'},
    "en": {' .pat @user': ' .pat @user'},
    "ua": {' .pat @user': ' .pat @user'}
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
        return texts["❌ .pat @user"]
    return ftexts["🖐 {args[0]}, тебя погладили по голове!"]



async def get_description():
    return {
        "ru": texts["Команда pat"],
        "en": texts["Command pat"],
        "ua": texts["Команда pat"]
    }
