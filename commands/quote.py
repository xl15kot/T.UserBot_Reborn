# quote.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'Будь изменением, которое хочешь видеть — Ганди': 'Будь изменением, которое хочешь видеть — Ганди', 'Жизнь — это то, что происходит, пока ты строишь планы — Леннон': 'Жизнь — это то, что происходит, пока ты строишь планы — Леннон', 'Единственный способ делать великую работу — любить то, что делаешь — Джобс': 'Единственный способ делать великую работу — любить то, что делаешь — Джобс', '💭 _{random.choice(quotes)}_': '💭 _{random.choice(quotes)}_', 'Команда quote': 'Команда quote', 'Command quote': 'Command quote'}

# quote.py
#Ru: Команда quote
#En: Command quote
#Ua: Команда quote

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
    quotes = [
        texts["Будь изменением, которое хочешь видеть — Ганди"],
        texts["Жизнь — это то, что происходит, пока ты строишь планы — Леннон"],
        texts["Единственный способ делать великую работу — любить то, что делаешь — Джобс"]
    ]
    return ftexts["💭 _{random.choice(quotes)}_"]



async def get_description():
    return {
        "ru": texts["Команда quote"],
        "en": texts["Command quote"],
        "ua": texts["Команда quote"]
    }
