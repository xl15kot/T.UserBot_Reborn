# deltodo.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .deltodo <номер>': ' .deltodo <номер>', 'lang_code': 'lang_code', '❌ .deltodo <номер>': '❌ .deltodo <номер>', 'DELETE FROM todos WHERE id=? AND user_id=?': 'DELETE FROM todos WHERE id=? AND user_id=?', '🗑 Задача #{tid} удалена': '🗑 Задача #{tid} удалена', 'Команда deltodo': 'Команда deltodo', 'Command deltodo': 'Command deltodo'}

# deltodo.py
#Ru: Команда deltodo
#En: Command deltodo
#Ua: Команда deltodo

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .deltodo <номер>': ' .deltodo <номер>'},
    "en": {' .deltodo <номер>': ' .deltodo <номер>'},
    "ua": {' .deltodo <номер>': ' .deltodo <номер>'}
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
        return texts["❌ .deltodo <номер>"]
    try:
        tid = int(args[0])
        db.c.execute(texts["DELETE FROM todos WHERE id=? AND user_id=?"], (tid, event.sender_id))
        db.conn.commit()
        return ftexts["🗑 Задача #{tid} удалена"]
    except:
        return texts["❌ .deltodo <номер>"]



async def get_description():
    return {
        "ru": texts["Команда deltodo"],
        "en": texts["Command deltodo"],
        "ua": texts["Команда deltodo"]
    }
