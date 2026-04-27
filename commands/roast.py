# roast.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .roast @user': ' .roast @user', 'lang_code': 'lang_code', '❌ .roast @user': '❌ .roast @user', '{} — ты как обновление Windows: все ждут, но никто не рад.': '{} — ты как обновление Windows: все ждут, но никто не рад.', '{} — твой IQ меньше температуры в комнате.': '{} — твой IQ меньше температуры в комнате.', '{} — даже Google не знает ответа на вопрос, зачем ты существуешь.': '{} — даже Google не знает ответа на вопрос, зачем ты существуешь.', '🔥 {random.choice(roasts).format(args[0])}': '🔥 {random.choice(roasts).format(args[0])}', 'Команда roast': 'Команда roast', 'Command roast': 'Command roast'}

# roast.py
#Ru: Команда roast
#En: Command roast
#Ua: Команда roast

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .roast @user': ' .roast @user'},
    "en": {' .roast @user': ' .roast @user'},
    "ua": {' .roast @user': ' .roast @user'}
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
        return texts["❌ .roast @user"]
    roasts = [
        texts["{} — ты как обновление Windows: все ждут, но никто не рад."],
        texts["{} — твой IQ меньше температуры в комнате."],
        texts["{} — даже Google не знает ответа на вопрос, зачем ты существуешь."]
    ]
    return ftexts["🔥 {random.choice(roasts).format(args[0])}"]



async def get_description():
    return {
        "ru": texts["Команда roast"],
        "en": texts["Command roast"],
        "ua": texts["Команда roast"]
    }
