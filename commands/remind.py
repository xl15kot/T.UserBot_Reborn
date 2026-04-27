# remind.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .remind <секунды> <текст>': ' .remind <секунды> <текст>', 'lang_code': 'lang_code', '❌ .remind <секунды> <текст>': '❌ .remind <секунды> <текст>', '⏰ Напоминание через {secs}с: {text}': '⏰ Напоминание через {secs}с: {text}', '🔔 **НАПОМИНАНИЕ!**\\n\\n{text}': '🔔 **НАПОМИНАНИЕ!**\\n\\n{text}', 'Команда remind': 'Команда remind', 'Command remind': 'Command remind'}

# remind.py
#Ru: Команда remind
#En: Command remind
#Ua: Команда remind

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .remind <секунды> <текст>': ' .remind <секунды> <текст>'},
    "en": {' .remind <секунды> <текст>': ' .remind <секунды> <текст>'},
    "ua": {' .remind <секунды> <текст>': ' .remind <секунды> <текст>'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if len(args) < 2:
        return texts["❌ .remind <секунды> <текст>"]
    try:
        secs = int(args[0])
        text = " ".join(args[1:])
        await event.edit(ftexts["⏰ Напоминание через {secs}с: {text}"])
        async def remind():
            await asyncio.sleep(secs)
            await event.respond(ftexts["🔔 **НАПОМИНАНИЕ!**\n\n{text}"])
        asyncio.create_task(remind())
        return None
    except:
        return texts["❌ .remind <секунды> <текст>"]



async def get_description():
    return {
        "ru": texts["Команда remind"],
        "en": texts["Command remind"],
        "ua": texts["Команда remind"]
    }
