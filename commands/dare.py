# dare.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'Напиши первому в контактах Я тебя люблю': 'Напиши первому в контактах Я тебя люблю', 'Расскажи свой самый неловкий момент': 'Расскажи свой самый неловкий момент', 'Отправь голосовое с пением 30 секунд': 'Отправь голосовое с пением 30 секунд', 'Поменяй аватарку на то, что скажет чат': 'Поменяй аватарку на то, что скажет чат', '🎭 **ДЕЙСТВИЕ:**\\n_{random.choice(dares)}_': '🎭 **ДЕЙСТВИЕ:**\\n_{random.choice(dares)}_', 'Команда dare': 'Команда dare', 'Command dare': 'Command dare'}

# dare.py
#Ru: Команда dare
#En: Command dare
#Ua: Команда dare

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
    dares = [
        "Напиши первому в контактах 'Я тебя люблю'",
        texts["Расскажи свой самый неловкий момент"],
        texts["Отправь голосовое с пением 30 секунд"],
        texts["Поменяй аватарку на то, что скажет чат"]
    ]
    return ftexts["🎭 **ДЕЙСТВИЕ:**\n_{random.choice(dares)}_"]



async def get_description():
    return {
        "ru": texts["Команда dare"],
        "en": texts["Command dare"],
        "ua": texts["Команда dare"]
    }
