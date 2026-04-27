# clear_cache.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' Кэш очищен!': ' Кэш очищен!', 'lang_code': 'lang_code', '🧹 Очистка кэша...': '🧹 Очистка кэша...', '__pycache__': '__pycache__', 'commands': 'commands', 'data/__pycache__': 'data/__pycache__', '✅ Кэш очищен!': '✅ Кэш очищен!', 'Команда clear_cache': 'Команда clear_cache', 'Command clear_cache': 'Command clear_cache'}

# clear_cache.py
#Ru: Команда clear_cache
#En: Command clear_cache
#Ua: Команда clear_cache

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' Кэш очищен!': ' Кэш очищен!'},
    "en": {' Кэш очищен!': ' Кэш очищен!'},
    "ua": {' Кэш очищен!': ' Кэш очищен!'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    await event.edit(texts["🧹 Очистка кэша..."])
    if os.path.exists(texts["__pycache__"]):
        shutil.rmtree(texts["__pycache__"])
    for root, dirs, files in os.walk(texts["commands"]):
        if texts["__pycache__"] in dirs:
            shutil.rmtree(os.path.join(root, texts["__pycache__"]))
    if os.path.exists(texts["data/__pycache__"]):
        shutil.rmtree(texts["data/__pycache__"])
    return texts["✅ Кэш очищен!"]


async def get_description():
    return {
        "ru": texts["Команда clear_cache"],
        "en": texts["Command clear_cache"],
        "ua": texts["Команда clear_cache"]
    }
