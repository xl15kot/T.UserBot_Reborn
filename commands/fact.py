# fact.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'Осьминог имеет 3 сердца! 🐙': 'Осьминог имеет 3 сердца! 🐙', 'Слоны не умеют прыгать 🐘': 'Слоны не умеют прыгать 🐘', 'Бананы — это ягоды 🍌': 'Бананы — это ягоды 🍌', 'Мёд никогда не портится 🍯': 'Мёд никогда не портится 🍯', 'Кошки проводят 70% жизни во сне 😴': 'Кошки проводят 70% жизни во сне 😴', '📚 {random.choice(facts)}': '📚 {random.choice(facts)}', 'Команда fact': 'Команда fact', 'Command fact': 'Command fact'}

# fact.py
#Ru: Команда fact
#En: Command fact
#Ua: Команда fact

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
    facts = [
        texts["Осьминог имеет 3 сердца! 🐙"],
        texts["Слоны не умеют прыгать 🐘"],
        texts["Бананы — это ягоды 🍌"],
        texts["Мёд никогда не портится 🍯"],
        texts["Кошки проводят 70% жизни во сне 😴"]
    ]
    return ftexts["📚 {random.choice(facts)}"]



async def get_description():
    return {
        "ru": texts["Команда fact"],
        "en": texts["Command fact"],
        "ua": texts["Команда fact"]
    }
