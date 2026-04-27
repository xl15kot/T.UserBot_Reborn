# fortytwo.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'🌌 Главный вопрос жизни, вселенной и вообще:\\\\n\\\\n**42**\\\\n\\\\n_— Автостопом по галактике_': '🌌 Главный вопрос жизни, вселенной и вообще:\\\\n\\\\n**42**\\\\n\\\\n_— Автостопом по галактике_', 'lang_code': 'lang_code', '🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_': '🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_', 'Команда fortytwo': 'Команда fortytwo', 'Command fortytwo': 'Command fortytwo'}

# fortytwo.py
#Ru: Команда fortytwo
#En: Command fortytwo
#Ua: Команда fortytwo

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {'🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_': '🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_'},
    "en": {'🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_': '🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_'},
    "ua": {'🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_': '🌌 Главный вопрос жизни, вселенной и вообще:\\n\\n**42**\\n\\n_— Автостопом по галактике_'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    return texts["🌌 Главный вопрос жизни, вселенной и вообще:\n\n**42**\n\n_— Автостопом по галактике_"]



async def get_description():
    return {
        "ru": texts["Команда fortytwo"],
        "en": texts["Command fortytwo"],
        "ua": texts["Команда fortytwo"]
    }
