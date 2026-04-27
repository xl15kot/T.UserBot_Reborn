# countdown.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .countdown <секунды>': ' .countdown <секунды>', 'lang_code': 'lang_code', '❌ .countdown <секунды>': '❌ .countdown <секунды>', '⏳ {i}': '⏳ {i}', '🚀 **СТАРТ!**': '🚀 **СТАРТ!**', 'Команда countdown': 'Команда countdown', 'Command countdown': 'Command countdown'}

# countdown.py
#Ru: Команда countdown
#En: Command countdown
#Ua: Команда countdown

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .countdown <секунды>': ' .countdown <секунды>'},
    "en": {' .countdown <секунды>': ' .countdown <секунды>'},
    "ua": {' .countdown <секунды>': ' .countdown <секунды>'}
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
        return texts["❌ .countdown <секунды>"]
    try:
        secs = int(args[0])
        for i in range(secs, 0, -1):
            await event.edit(ftexts["⏳ {i}"])
            await asyncio.sleep(1)
        await event.edit(texts["🚀 **СТАРТ!**"])
        return None
    except:
        return texts["❌ .countdown <секунды>"]



async def get_description():
    return {
        "ru": texts["Команда countdown"],
        "en": texts["Command countdown"],
        "ua": texts["Команда countdown"]
    }
