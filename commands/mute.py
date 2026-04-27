# mute.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .mute @user': ' .mute @user', 'lang_code': 'lang_code', '❌ .mute @user': '❌ .mute @user', '🔇 {args[0]} замучен (симуляция)': '🔇 {args[0]} замучен (симуляция)', 'Команда mute': 'Команда mute', 'Command mute': 'Command mute'}

# mute.py
#Ru: Команда mute
#En: Command mute
#Ua: Команда mute

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .mute @user': ' .mute @user'},
    "en": {' .mute @user': ' .mute @user'},
    "ua": {' .mute @user': ' .mute @user'}
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
        return texts["❌ .mute @user"]
    return ftexts["🔇 {args[0]} замучен (симуляция)"]



async def get_description():
    return {
        "ru": texts["Команда mute"],
        "en": texts["Command mute"],
        "ua": texts["Команда mute"]
    }
