# compliment.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .compliment @user': ' .compliment @user', 'lang_code': 'lang_code', '❌ .compliment @user': '❌ .compliment @user', '{} — ты как Wi-Fi: соединяешь сердца! 💕': '{} — ты как Wi-Fi: соединяешь сердца! 💕', '{} — твоя улыбка лучшее, что есть в этом мире! 😊': '{} — твоя улыбка лучшее, что есть в этом мире! 😊', '{} — ты как хороший код: красивый и эффективный! 💻': '{} — ты как хороший код: красивый и эффективный! 💻', '💝 {random.choice(compliments).format(args[0])}': '💝 {random.choice(compliments).format(args[0])}', 'Команда compliment': 'Команда compliment', 'Command compliment': 'Command compliment'}

# compliment.py
#Ru: Команда compliment
#En: Command compliment
#Ua: Команда compliment

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .compliment @user': ' .compliment @user'},
    "en": {' .compliment @user': ' .compliment @user'},
    "ua": {' .compliment @user': ' .compliment @user'}
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
        return texts["❌ .compliment @user"]
    compliments = [
        texts["{} — ты как Wi-Fi: соединяешь сердца! 💕"],
        texts["{} — твоя улыбка лучшее, что есть в этом мире! 😊"],
        texts["{} — ты как хороший код: красивый и эффективный! 💻"]
    ]
    return ftexts["💝 {random.choice(compliments).format(args[0])}"]



async def get_description():
    return {
        "ru": texts["Команда compliment"],
        "en": texts["Command compliment"],
        "ua": texts["Команда compliment"]
    }
