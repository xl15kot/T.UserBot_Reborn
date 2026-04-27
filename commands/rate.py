# rate.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .rate @user': ' .rate @user', 'lang_code': 'lang_code', '❌ .rate @user': '❌ .rate @user', '⭐ {args[0]}: {random.randint(0,10)}/10': '⭐ {args[0]}: {random.randint(0,10)}/10', 'Команда rate': 'Команда rate', 'Command rate': 'Command rate'}

# rate.py
#Ru: Команда rate
#En: Command rate
#Ua: Команда rate

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .rate @user': ' .rate @user'},
    "en": {' .rate @user': ' .rate @user'},
    "ua": {' .rate @user': ' .rate @user'}
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
        return texts["❌ .rate @user"]
    return ftexts["⭐ {args[0]}: {random.randint(0,10)}/10"]



async def get_description():
    return {
        "ru": texts["Команда rate"],
        "en": texts["Command rate"],
        "ua": texts["Команда rate"]
    }
