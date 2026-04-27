# fakeban.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .fakeban @user': ' .fakeban @user', 'lang_code': 'lang_code', '❌ .fakeban @user': '❌ .fakeban @user', '🔨 {args[0]} ЗАБАНЕН!': '🔨 {args[0]} ЗАБАНЕН!', '😂 Шутка! {args[0]} не забанен': '😂 Шутка! {args[0]} не забанен', 'Команда fakeban': 'Команда fakeban', 'Command fakeban': 'Command fakeban'}

# fakeban.py
#Ru: Команда fakeban
#En: Command fakeban
#Ua: Команда fakeban

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .fakeban @user': ' .fakeban @user'},
    "en": {' .fakeban @user': ' .fakeban @user'},
    "ua": {' .fakeban @user': ' .fakeban @user'}
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
        return texts["❌ .fakeban @user"]
    await event.delete()
    msg = await event.respond(ftexts["🔨 {args[0]} ЗАБАНЕН!"])
    await asyncio.sleep(3)
    await msg.edit(ftexts["😂 Шутка! {args[0]} не забанен"])
    return None



async def get_description():
    return {
        "ru": texts["Команда fakeban"],
        "en": texts["Command fakeban"],
        "ua": texts["Команда fakeban"]
    }
