# unmute.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .unmute @user': ' .unmute @user', 'lang_code': 'lang_code', '❌ .unmute @user': '❌ .unmute @user', '🔊 {args[0]} размучен (симуляция)': '🔊 {args[0]} размучен (симуляция)', 'Команда unmute': 'Команда unmute', 'Command unmute': 'Command unmute'}

# unmute.py
#Ru: Команда unmute
#En: Command unmute
#Ua: Команда unmute

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .unmute @user': ' .unmute @user'},
    "en": {' .unmute @user': ' .unmute @user'},
    "ua": {' .unmute @user': ' .unmute @user'}
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
        return texts["❌ .unmute @user"]
    return ftexts["🔊 {args[0]} размучен (симуляция)"]



async def get_description():
    return {
        "ru": texts["Команда unmute"],
        "en": texts["Command unmute"],
        "ua": texts["Команда unmute"]
    }
