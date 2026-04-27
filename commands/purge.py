# purge.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .purge <количество>': ' .purge <количество>', 'lang_code': 'lang_code', '❌ .purge <количество>': '❌ .purge <количество>', '✅ Удалено {n} сообщений (симуляция)': '✅ Удалено {n} сообщений (симуляция)', 'Команда purge': 'Команда purge', 'Command purge': 'Command purge'}

# purge.py
#Ru: Команда purge
#En: Command purge
#Ua: Команда purge

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .purge <количество>': ' .purge <количество>'},
    "en": {' .purge <количество>': ' .purge <количество>'},
    "ua": {' .purge <количество>': ' .purge <количество>'}
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
        return texts["❌ .purge <количество>"]
    try:
        n = min(int(args[0]), 50)
        await event.delete()
        tmp = await event.respond(ftexts["✅ Удалено {n} сообщений (симуляция)"])
        await asyncio.sleep(3)
        await tmp.delete()
        return None
    except:
        return texts["❌ .purge <количество>"]



async def get_description():
    return {
        "ru": texts["Команда purge"],
        "en": texts["Command purge"],
        "ua": texts["Команда purge"]
    }
