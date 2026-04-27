# donetodo.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .donetodo <номер>': ' .donetodo <номер>', 'lang_code': 'lang_code', '❌ .donetodo <номер>': '❌ .donetodo <номер>', 'UPDATE todos SET done=1 WHERE id=? AND user_id=?': 'UPDATE todos SET done=1 WHERE id=? AND user_id=?', '✅ Задача #{tid} выполнена!': '✅ Задача #{tid} выполнена!', 'Команда donetodo': 'Команда donetodo', 'Command donetodo': 'Command donetodo'}

# donetodo.py
#Ru: Команда donetodo
#En: Command donetodo
#Ua: Команда donetodo

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .donetodo <номер>': ' .donetodo <номер>'},
    "en": {' .donetodo <номер>': ' .donetodo <номер>'},
    "ua": {' .donetodo <номер>': ' .donetodo <номер>'}
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
        return texts["❌ .donetodo <номер>"]
    try:
        tid = int(args[0])
        db.c.execute(texts["UPDATE todos SET done=1 WHERE id=? AND user_id=?"], (tid, event.sender_id))
        db.conn.commit()
        return ftexts["✅ Задача #{tid} выполнена!"]
    except:
        return texts["❌ .donetodo <номер>"]



async def get_description():
    return {
        "ru": texts["Команда donetodo"],
        "en": texts["Command donetodo"],
        "ua": texts["Команда donetodo"]
    }
