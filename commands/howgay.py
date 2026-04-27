# howgay.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .howgay @user': ' .howgay @user', 'lang_code': 'lang_code', '❌ .howgay @user': '❌ .howgay @user', '🌈 {args[0]} гей на {random.randint(0,100)}%': '🌈 {args[0]} гей на {random.randint(0,100)}%', 'Команда howgay': 'Команда howgay', 'Command howgay': 'Command howgay'}

# howgay.py
#Ru: Команда howgay
#En: Command howgay
#Ua: Команда howgay

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .howgay @user': ' .howgay @user'},
    "en": {' .howgay @user': ' .howgay @user'},
    "ua": {' .howgay @user': ' .howgay @user'}
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
        return texts["❌ .howgay @user"]
    return ftexts["🌈 {args[0]} гей на {random.randint(0,100)}%"]



async def get_description():
    return {
        "ru": texts["Команда howgay"],
        "en": texts["Command howgay"],
        "ua": texts["Команда howgay"]
    }
