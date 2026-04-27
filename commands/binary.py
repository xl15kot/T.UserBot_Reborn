# binary.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .binary <текст>': ' .binary <текст>', 'lang_code': 'lang_code', '❌ .binary <текст>': '❌ .binary <текст>', '💾 `{  .join(f{ord(c):08b} for c in text)}`': '💾 `{  .join(f{ord(c):08b} for c in text)}`', 'Команда binary': 'Команда binary', 'Command binary': 'Command binary'}

# binary.py
#Ru: Команда binary
#En: Command binary
#Ua: Команда binary

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .binary <текст>': ' .binary <текст>'},
    "en": {' .binary <текст>': ' .binary <текст>'},
    "ua": {' .binary <текст>': ' .binary <текст>'}
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
        return texts["❌ .binary <текст>"]
    text = " ".join(args)
    return f"💾 `{'  '.join(f'{ord(c):08b}' for c in text)}`"



async def get_description():
    return {
        "ru": texts["Команда binary"],
        "en": texts["Command binary"],
        "ua": texts["Команда binary"]
    }
