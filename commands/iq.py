# iq.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .iq @user': ' .iq @user', 'lang_code': 'lang_code', '❌ .iq @user': '❌ .iq @user', 'Гений': 'Гений', 'Умный': 'Умный', 'Средний': 'Средний', 'Ниже среднего': 'Ниже среднего', '🧠 IQ {args[0]}: **{iq}**\\nУровень: {lvl}': '🧠 IQ {args[0]}: **{iq}**\\nУровень: {lvl}', 'Команда iq': 'Команда iq', 'Command iq': 'Command iq'}

# iq.py
#Ru: Команда iq
#En: Command iq
#Ua: Команда iq

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .iq @user': ' .iq @user'},
    "en": {' .iq @user': ' .iq @user'},
    "ua": {' .iq @user': ' .iq @user'}
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
        return texts["❌ .iq @user"]
    iq = random.randint(40, 200)
    lvl = texts["Гений"] if iq > 140 else texts["Умный"] if iq > 110 else texts["Средний"] if iq > 85 else texts["Ниже среднего"]
    return ftexts["🧠 IQ {args[0]}: **{iq}**\nУровень: {lvl}"]



async def get_description():
    return {
        "ru": texts["Команда iq"],
        "en": texts["Command iq"],
        "ua": texts["Команда iq"]
    }
