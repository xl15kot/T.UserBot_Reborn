# ship.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .ship @user1 @user2': ' .ship @user1 @user2', 'lang_code': 'lang_code', '❌ .ship @user1 @user2': '❌ .ship @user1 @user2', '💕 {args[0]} + {args[1]} = {random.randint(0,100)}%': '💕 {args[0]} + {args[1]} = {random.randint(0,100)}%', 'Команда ship': 'Команда ship', 'Command ship': 'Command ship'}

# ship.py
#Ru: Команда ship
#En: Command ship
#Ua: Команда ship

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .ship @user1 @user2': ' .ship @user1 @user2'},
    "en": {' .ship @user1 @user2': ' .ship @user1 @user2'},
    "ua": {' .ship @user1 @user2': ' .ship @user1 @user2'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if len(args) < 2:
        return texts["❌ .ship @user1 @user2"]
    return ftexts["💕 {args[0]} + {args[1]} = {random.randint(0,100)}%"]



async def get_description():
    return {
        "ru": texts["Команда ship"],
        "en": texts["Command ship"],
        "ua": texts["Команда ship"]
    }
