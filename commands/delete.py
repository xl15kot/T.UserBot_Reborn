# delete.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'Команда delete': 'Команда delete', 'Command delete': 'Command delete'}

# delete.py
#Ru: Команда delete
#En: Command delete
#Ua: Команда delete

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
    if event.is_reply:
        r = await event.get_reply_message()
        await r.delete()
    await event.delete()
    return None



async def get_description():
    return {
        "ru": texts["Команда delete"],
        "en": texts["Command delete"],
        "ua": texts["Команда delete"]
    }
