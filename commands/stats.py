# stats.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'SELECT SUM(count) FROM cmd_stats': 'SELECT SUM(count) FROM cmd_stats', '📊 **Статистика**\\n🔥 Команд использовано: {total}\\n📦 Команд доступно: 2000+\\n🍵 TeaDevs': '📊 **Статистика**\\n🔥 Команд использовано: {total}\\n📦 Команд доступно: 2000+\\n🍵 TeaDevs', 'Команда stats': 'Команда stats', 'Command stats': 'Command stats'}

# stats.py
#Ru: Команда stats
#En: Command stats
#Ua: Команда stats

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
    db.c.execute(texts["SELECT SUM(count) FROM cmd_stats"])
    total = db.c.fetchone()[0] or 0
    return ftexts["📊 **Статистика**\n🔥 Команд использовано: {total}\n📦 Команд доступно: 2000+\n🍵 TeaDevs"]



async def get_description():
    return {
        "ru": texts["Команда stats"],
        "en": texts["Command stats"],
        "ua": texts["Команда stats"]
    }
