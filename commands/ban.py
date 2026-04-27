# ban.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .ban @user': ' .ban @user', 'lang_code': 'lang_code', '❌ .ban @user': '❌ .ban @user', '🔨 {args[0]} забанен (симуляция)': '🔨 {args[0]} забанен (симуляция)', 'Команда ban': 'Команда ban', 'Command ban': 'Command ban'}

# ban.py
#Ru: Команда ban
#En: Command ban
#Ua: Команда ban

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .ban @user': ' .ban @user'},
    "en": {' .ban @user': ' .ban @user'},
    "ua": {' .ban @user': ' .ban @user'}
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
        return texts["❌ .ban @user"]
    return ftexts["🔨 {args[0]} забанен (симуляция)"]



async def get_description():
    return {
        "ru": texts["Команда ban"],
        "en": texts["Command ban"],
        "ua": texts["Команда ban"]
    }
