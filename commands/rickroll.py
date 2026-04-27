# rickroll.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'🎵 Never gonna give you up 🎶\\\\nhttps://youtu.be/dQw4w9WgXcQ': '🎵 Never gonna give you up 🎶\\\\nhttps://youtu.be/dQw4w9WgXcQ', 'lang_code': 'lang_code', '🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ': '🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ', 'Команда rickroll': 'Команда rickroll', 'Command rickroll': 'Command rickroll'}

# rickroll.py
#Ru: Команда rickroll
#En: Command rickroll
#Ua: Команда rickroll

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {'🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ': '🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ'},
    "en": {'🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ': '🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ'},
    "ua": {'🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ': '🎵 Never gonna give you up 🎶\\nhttps://youtu.be/dQw4w9WgXcQ'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    return texts["🎵 Never gonna give you up 🎶\nhttps://youtu.be/dQw4w9WgXcQ"]



async def get_description():
    return {
        "ru": texts["Команда rickroll"],
        "en": texts["Command rickroll"],
        "ua": texts["Команда rickroll"]
    }
