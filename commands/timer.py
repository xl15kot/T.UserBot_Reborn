# timer.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .timer <секунды>': ' .timer <секунды>', 'lang_code': 'lang_code', '❌ .timer <секунды>': '❌ .timer <секунды>', '⏰ Таймер: {secs}с': '⏰ Таймер: {secs}с', '⏰ Таймер: {i}с': '⏰ Таймер: {i}с', '🔔 **ВРЕМЯ ВЫШЛО!**': '🔔 **ВРЕМЯ ВЫШЛО!**', 'Команда timer': 'Команда timer', 'Command timer': 'Command timer'}

# timer.py
#Ru: Команда timer
#En: Command timer
#Ua: Команда timer

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .timer <секунды>': ' .timer <секунды>'},
    "en": {' .timer <секунды>': ' .timer <секунды>'},
    "ua": {' .timer <секунды>': ' .timer <секунды>'}
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
        return texts["❌ .timer <секунды>"]
    try:
        secs = int(args[0])
        msg = await event.edit(ftexts["⏰ Таймер: {secs}с"])
        for i in range(secs-1, 0, -1):
            await asyncio.sleep(1)
            if i <= 5 or i % 10 == 0:
                await msg.edit(ftexts["⏰ Таймер: {i}с"])
        await msg.edit(texts["🔔 **ВРЕМЯ ВЫШЛО!**"])
        return None
    except:
        return texts["❌ .timer <секунды>"]



async def get_description():
    return {
        "ru": texts["Команда timer"],
        "en": texts["Command timer"],
        "ua": texts["Команда timer"]
    }
