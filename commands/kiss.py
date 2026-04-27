# kiss.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .kiss @user': ' .kiss @user', 'lang_code': 'lang_code', '❌ .kiss @user': '❌ .kiss @user', '😘 {args[0]}, ты получил поцелуй!': '😘 {args[0]}, ты получил поцелуй!', 'Команда kiss': 'Команда kiss', 'Command kiss': 'Command kiss'}

# kiss.py
#Ru: Команда kiss
#En: Command kiss
#Ua: Команда kiss

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .kiss @user': ' .kiss @user'},
    "en": {' .kiss @user': ' .kiss @user'},
    "ua": {' .kiss @user': ' .kiss @user'}
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
        return texts["❌ .kiss @user"]
    return ftexts["😘 {args[0]}, ты получил поцелуй!"]



async def get_description():
    return {
        "ru": texts["Команда kiss"],
        "en": texts["Command kiss"],
        "ua": texts["Команда kiss"]
    }
