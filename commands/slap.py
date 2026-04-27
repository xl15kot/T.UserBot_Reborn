# slap.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .slap @user': ' .slap @user', 'lang_code': 'lang_code', '❌ .slap @user': '❌ .slap @user', '👋 {args[0]}, ты получил пощёчину!': '👋 {args[0]}, ты получил пощёчину!', 'Команда slap': 'Команда slap', 'Command slap': 'Command slap'}

# slap.py
#Ru: Команда slap
#En: Command slap
#Ua: Команда slap

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .slap @user': ' .slap @user'},
    "en": {' .slap @user': ' .slap @user'},
    "ua": {' .slap @user': ' .slap @user'}
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
        return texts["❌ .slap @user"]
    return ftexts["👋 {args[0]}, ты получил пощёчину!"]



async def get_description():
    return {
        "ru": texts["Команда slap"],
        "en": texts["Command slap"],
        "ua": texts["Команда slap"]
    }
