# propose.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .propose @user': ' .propose @user', 'lang_code': 'lang_code', '❌ .propose @user': '❌ .propose @user', '💍 {args[0]}, выйди за меня! 💍': '💍 {args[0]}, выйди за меня! 💍', 'Команда propose': 'Команда propose', 'Command propose': 'Command propose'}

# propose.py
#Ru: Команда propose
#En: Command propose
#Ua: Команда propose

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .propose @user': ' .propose @user'},
    "en": {' .propose @user': ' .propose @user'},
    "ua": {' .propose @user': ' .propose @user'}
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
        return texts["❌ .propose @user"]
    return ftexts["💍 {args[0]}, выйди за меня! 💍"]



async def get_description():
    return {
        "ru": texts["Команда propose"],
        "en": texts["Command propose"],
        "ua": texts["Команда propose"]
    }
