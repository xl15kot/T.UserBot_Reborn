# about.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', '👨\u200d💻 **Разработчики:** AveBas, LimuxMintREAL\\n🍵 TeaDevs\\n🧪 **Тестеры:** Ariy228, DarkSteem, Jester777\\n📦 Команд: 2000+': '👨\u200d💻 **Разработчики:** AveBas, LimuxMintREAL\\n🍵 TeaDevs\\n🧪 **Тестеры:** Ariy228, DarkSteem, Jester777\\n📦 Команд: 2000+', 'Команда about': 'Команда about', 'Command about': 'Command about'}

# about.py
#Ru: Команда about
#En: Command about
#Ua: Команда about

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
    return ftexts["👨‍💻 **Разработчики:** AveBas, LimuxMintREAL\n🍵 TeaDevs\n🧪 **Тестеры:** Ariy228, DarkSteem, Jester777\n📦 Команд: 2000+"]



async def get_description():
    return {
        "ru": texts["Команда about"],
        "en": texts["Command about"],
        "ua": texts["Команда about"]
    }
