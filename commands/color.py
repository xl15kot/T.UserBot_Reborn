# color.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', '#{random.randint(0,0xFFFFFF):06x}': '#{random.randint(0,0xFFFFFF):06x}', '🎨 HEX: `{hx}`': '🎨 HEX: `{hx}`', 'Команда color': 'Команда color', 'Command color': 'Command color'}

# color.py
#Ru: Команда color
#En: Command color
#Ua: Команда color

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
    hx = ftexts["#{random.randint(0,0xFFFFFF):06x}"]
    return ftexts["🎨 HEX: `{hx}`"]



async def get_description():
    return {
        "ru": texts["Команда color"],
        "en": texts["Command color"],
        "ua": texts["Команда color"]
    }
