# type.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .type <текст>': ' .type <текст>', 'lang_code': 'lang_code', '❌ .type <текст>': '❌ .type <текст>', 'Команда type': 'Команда type', 'Command type': 'Command type'}

# type.py
#Ru: Команда type
#En: Command type
#Ua: Команда type

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .type <текст>': ' .type <текст>'},
    "en": {' .type <текст>': ' .type <текст>'},
    "ua": {' .type <текст>': ' .type <текст>'}
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
        return texts["❌ .type <текст>"]
    text = " ".join(args)
    msg = await event.edit("▒")
    typed = ""
    for ch in text:
        typed += ch
        await msg.edit(typed + "▒")
        await asyncio.sleep(0.06)
    await msg.edit(typed)
    return None



async def get_description():
    return {
        "ru": texts["Команда type"],
        "en": texts["Command type"],
        "ua": texts["Команда type"]
    }
