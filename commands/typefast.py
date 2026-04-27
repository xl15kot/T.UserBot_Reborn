# typefast.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .typefast <текст>': ' .typefast <текст>', 'lang_code': 'lang_code', '❌ .typefast <текст>': '❌ .typefast <текст>', 'Команда typefast': 'Команда typefast', 'Command typefast': 'Command typefast'}

# typefast.py
#Ru: Команда typefast
#En: Command typefast
#Ua: Команда typefast

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .typefast <текст>': ' .typefast <текст>'},
    "en": {' .typefast <текст>': ' .typefast <текст>'},
    "ua": {' .typefast <текст>': ' .typefast <текст>'}
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
        return texts["❌ .typefast <текст>"]
    text = " ".join(args)
    msg = await event.edit("▒")
    typed = ""
    for ch in text:
        typed += ch
        await msg.edit(typed + "▒")
        await asyncio.sleep(0.025)
    await msg.edit(typed)
    return None



async def get_description():
    return {
        "ru": texts["Команда typefast"],
        "en": texts["Command typefast"],
        "ua": texts["Команда typefast"]
    }
