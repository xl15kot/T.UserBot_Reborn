# matrix.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', '`01001000 01100101`': '`01001000 01100101`', '`01001000 01100101 01101100`': '`01001000 01100101 01101100`', '`01001000 01100101 01101100 01101100`': '`01001000 01100101 01101100 01101100`', '`01001000 01100101 01101100 01101100 01101111`\\n\\n🤖 Hello World!': '`01001000 01100101 01101100 01101100 01101111`\\n\\n🤖 Привет Мир!', '💊 THE MATRIX': '💊 THE MATRIX', '💊 THE MATRIX\\n{f}': '💊 THE MATRIX\\n{f}', 'Команда matrix': 'Команда matrix', 'Command matrix': 'Command matrix'}

# matrix.py
#Ru: Команда matrix
#En: Command matrix
#Ua: Команда matrix

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
    frames = [
        texts["`01001000 01100101`"],
        texts["`01001000 01100101 01101100`"],
        texts["`01001000 01100101 01101100 01101100`"],
        texts["`01001000 01100101 01101100 01101100 01101111`\n\n🤖 Hello World!"]
    ]
    msg = await event.edit(texts["💊 THE MATRIX"])
    for f in frames:
        await asyncio.sleep(0.6)
        await msg.edit(ftexts["💊 THE MATRIX\n{f}"])
    return None



async def get_description():
    return {
        "ru": texts["Команда matrix"],
        "en": texts["Command matrix"],
        "ua": texts["Команда matrix"]
    }
