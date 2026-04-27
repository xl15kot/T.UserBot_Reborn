# bonk.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .bonk @user': ' .bonk @user', 'lang_code': 'lang_code', '❌ .bonk @user': '❌ .bonk @user', '🔨 {args[0]} отправлен в рогалик!': '🔨 {args[0]} отправлен в рогалик!', 'Команда bonk': 'Команда bonk', 'Command bonk': 'Command bonk'}

# bonk.py
#Ru: Команда bonk
#En: Command bonk
#Ua: Команда bonk

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .bonk @user': ' .bonk @user'},
    "en": {' .bonk @user': ' .bonk @user'},
    "ua": {' .bonk @user': ' .bonk @user'}
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
        return texts["❌ .bonk @user"]
    return ftexts["🔨 {args[0]} отправлен в рогалик!"]



async def get_description():
    return {
        "ru": texts["Команда bonk"],
        "en": texts["Command bonk"],
        "ua": texts["Команда bonk"]
    }
