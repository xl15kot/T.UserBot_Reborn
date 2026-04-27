# stop_bot.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', '🛑 Выключение...': '🛑 Выключение...', 'Команда stop_bot': 'Команда stop_bot', 'Command stop_bot': 'Command stop_bot'}

# stop_bot.py
#Ru: Команда stop_bot
#En: Command stop_bot
#Ua: Команда stop_bot

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {},
    "en": {},
    "ua": {}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    await event.edit(texts["🛑 Выключение..."])
    sys.exit(0)


async def get_description():
    return {
        "ru": texts["Команда stop_bot"],
        "en": texts["Command stop_bot"],
        "ua": texts["Команда stop_bot"]
    }
