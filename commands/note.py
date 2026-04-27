# note.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .note <название> <текст>': ' .note <название> <текст>', 'lang_code': 'lang_code', '❌ .note <название> <текст>': '❌ .note <название> <текст>', 'INSERT INTO notes (user_id, title, content, created) VALUES (?,?,?,?)': 'INSERT INTO notes (user_id, title, content, created) VALUES (?,?,?,?)', '✅ Заметка {title} сохранена!': '✅ Заметка {title} сохранена!', 'Команда note': 'Команда note', 'Command note': 'Command note'}

# note.py
#Ru: Команда note
#En: Command note
#Ua: Команда note

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .note <название> <текст>': ' .note <название> <текст>'},
    "en": {' .note <название> <текст>': ' .note <название> <текст>'},
    "ua": {' .note <название> <текст>': ' .note <название> <текст>'}
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
        return texts["❌ .note <название> <текст>"]
    title = args[0]
    content = " ".join(args[1:])
    db.c.execute(texts["INSERT INTO notes (user_id, title, content, created) VALUES (?,?,?,?)"],
                (event.sender_id, title, content, time.time()))
    db.conn.commit()
    return f"✅ Заметка '{title}' сохранена!"



async def get_description():
    return {
        "ru": texts["Команда note"],
        "en": texts["Command note"],
        "ua": texts["Команда note"]
    }
