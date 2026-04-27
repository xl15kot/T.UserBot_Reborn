# deln.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .deln <название>': ' .deln <название>', 'lang_code': 'lang_code', '❌ .deln <название>': '❌ .deln <название>', 'DELETE FROM notes WHERE user_id=? AND title=?': 'DELETE FROM notes WHERE user_id=? AND title=?', '🗑 Заметка {args[0]} удалена': '🗑 Заметка {args[0]} удалена', 'Команда deln': 'Команда deln', 'Command deln': 'Command deln'}

# deln.py
#Ru: Команда deln
#En: Command deln
#Ua: Команда deln

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .deln <название>': ' .deln <название>'},
    "en": {' .deln <название>': ' .deln <название>'},
    "ua": {' .deln <название>': ' .deln <название>'}
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
        return texts["❌ .deln <название>"]
    db.c.execute(texts["DELETE FROM notes WHERE user_id=? AND title=?"], (event.sender_id, args[0]))
    db.conn.commit()
    return f"🗑 Заметка '{args[0]}' удалена"



async def get_description():
    return {
        "ru": texts["Команда deln"],
        "en": texts["Command deln"],
        "ua": texts["Команда deln"]
    }
