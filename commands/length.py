# length.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .length <текст>': ' .length <текст>', 'lang_code': 'lang_code', '❌ .length <текст>': '❌ .length <текст>', '📏 {len( .join(args))} символов': '📏 {len( .join(args))} символов', 'Команда length': 'Команда length', 'Command length': 'Command length'}

# length.py
#Ru: Команда length
#En: Command length
#Ua: Команда length

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .length <текст>': ' .length <текст>'},
    "en": {' .length <текст>': ' .length <текст>'},
    "ua": {' .length <текст>': ' .length <текст>'}
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
        return texts["❌ .length <текст>"]
    return f"📏 {len(' '.join(args))} символов"



async def get_description():
    return {
        "ru": texts["Команда length"],
        "en": texts["Command length"],
        "ua": texts["Команда length"]
    }
