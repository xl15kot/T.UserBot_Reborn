# unban.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .unban @user': ' .unban @user', 'lang_code': 'lang_code', '❌ .unban @user': '❌ .unban @user', '🔓 {args[0]} разбанен (симуляция)': '🔓 {args[0]} разбанен (симуляция)', 'Команда unban': 'Команда unban', 'Command unban': 'Command unban'}

# unban.py
#Ru: Команда unban
#En: Command unban
#Ua: Команда unban

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .unban @user': ' .unban @user'},
    "en": {' .unban @user': ' .unban @user'},
    "ua": {' .unban @user': ' .unban @user'}
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
        return texts["❌ .unban @user"]
    return ftexts["🔓 {args[0]} разбанен (симуляция)"]



async def get_description():
    return {
        "ru": texts["Команда unban"],
        "en": texts["Command unban"],
        "ua": texts["Команда unban"]
    }
