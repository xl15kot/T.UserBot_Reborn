# hug.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .hug @user': ' .hug @user', 'lang_code': 'lang_code', '❌ .hug @user': '❌ .hug @user', '🤗 {args[0]}, ты получил обнимашки!': '🤗 {args[0]}, ты получил обнимашки!', 'Команда hug': 'Команда hug', 'Command hug': 'Command hug'}

# hug.py
#Ru: Команда hug
#En: Command hug
#Ua: Команда hug

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .hug @user': ' .hug @user'},
    "en": {' .hug @user': ' .hug @user'},
    "ua": {' .hug @user': ' .hug @user'}
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
        return texts["❌ .hug @user"]
    return ftexts["🤗 {args[0]}, ты получил обнимашки!"]



async def get_description():
    return {
        "ru": texts["Команда hug"],
        "en": texts["Command hug"],
        "ua": texts["Команда hug"]
    }
