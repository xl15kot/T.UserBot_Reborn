# todo.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .todo <текст>': ' .todo <текст>', 'lang_code': 'lang_code', '❌ .todo <текст>': '❌ .todo <текст>', 'INSERT INTO todos (user_id, task) VALUES (?,?)': 'INSERT INTO todos (user_id, task) VALUES (?,?)', '✅ Задача #{tid} добавлена: {task}': '✅ Задача #{tid} добавлена: {task}', 'Команда todo': 'Команда todo', 'Command todo': 'Command todo'}

# todo.py
#Ru: Команда todo
#En: Command todo
#Ua: Команда todo

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .todo <текст>': ' .todo <текст>'},
    "en": {' .todo <текст>': ' .todo <текст>'},
    "ua": {' .todo <текст>': ' .todo <текст>'}
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
        return texts["❌ .todo <текст>"]
    task = " ".join(args)
    db.c.execute(texts["INSERT INTO todos (user_id, task) VALUES (?,?)"], (event.sender_id, task))
    db.conn.commit()
    tid = db.c.lastrowid
    return ftexts["✅ Задача #{tid} добавлена: {task}"]



async def get_description():
    return {
        "ru": texts["Команда todo"],
        "en": texts["Command todo"],
        "ua": texts["Команда todo"]
    }
