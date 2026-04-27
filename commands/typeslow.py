# typeslow.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .typeslow <текст>': ' .typeslow <текст>', 'lang_code': 'lang_code', '❌ .typeslow <текст>': '❌ .typeslow <текст>', 'Команда typeslow': 'Команда typeslow', 'Command typeslow': 'Command typeslow'}

# typeslow.py
#Ru: Команда typeslow
#En: Command typeslow
#Ua: Команда typeslow

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .typeslow <текст>': ' .typeslow <текст>'},
    "en": {' .typeslow <текст>': ' .typeslow <текст>'},
    "ua": {' .typeslow <текст>': ' .typeslow <текст>'}
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
        return texts["❌ .typeslow <текст>"]
    text = " ".join(args)
    msg = await event.edit("▒")
    typed = ""
    for ch in text:
        typed += ch
        await msg.edit(typed + "▒")
        await asyncio.sleep(0.18)
    await msg.edit(typed)
    return None



async def get_description():
    return {
        "ru": texts["Команда typeslow"],
        "en": texts["Command typeslow"],
        "ua": texts["Команда typeslow"]
    }
