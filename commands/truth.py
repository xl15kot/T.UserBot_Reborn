# truth.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'Какой твой самый неловкий момент?': 'Какой твой самый неловкий момент?', 'Врал ли ты когда-нибудь учителю?': 'Врал ли ты когда-нибудь учителю?', 'Кто тебе нравится?': 'Кто тебе нравится?', 'Твой худший поступок в жизни?': 'Твой худший поступок в жизни?', '🔮 **ПРАВДА:**\\n_{random.choice(truths)}_': '🔮 **ПРАВДА:**\\n_{random.choice(truths)}_', 'Команда truth': 'Команда truth', 'Command truth': 'Command truth'}

# truth.py
#Ru: Команда truth
#En: Command truth
#Ua: Команда truth

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
    truths = [
        texts["Какой твой самый неловкий момент?"],
        texts["Врал ли ты когда-нибудь учителю?"],
        texts["Кто тебе нравится?"],
        texts["Твой худший поступок в жизни?"]
    ]
    return ftexts["🔮 **ПРАВДА:**\n_{random.choice(truths)}_"]



async def get_description():
    return {
        "ru": texts["Команда truth"],
        "en": texts["Command truth"],
        "ua": texts["Команда truth"]
    }
