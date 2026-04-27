# morse.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .morse <текст>': ' .morse <текст>', 'lang_code': 'lang_code', '❌ .morse <текст>': '❌ .morse <текст>', '-...': '-...', '-.-.': '-.-.', '..-.': '..-.', '....': '....', '.---': '.---', '.-..': '.-..', '.--.': '.--.', '--.-': '--.-', '...-': '...-', '-..-': '-..-', '-.--': '-.--', '--..': '--..', '📡 `{result}`': '📡 `{result}`', 'Команда morse': 'Команда morse', 'Command morse': 'Command morse'}

# morse.py
#Ru: Команда morse
#En: Command morse
#Ua: Команда morse

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .morse <текст>': ' .morse <текст>'},
    "en": {' .morse <текст>': ' .morse <текст>'},
    "ua": {' .morse <текст>': ' .morse <текст>'}
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
        return texts["❌ .morse <текст>"]
    m = {"a":".-","b":texts["-..."],"c":texts["-.-."],"d":"-..","e":".","f":texts["..-."],"g":"--.","h":texts["...."],"i":"..","j":texts[".---"],"k":"-.-","l":texts[".-.."],"m":"--","n":"-.","o":"---","p":texts[".--."],"q":texts["--.-"],"r":".-.","s":"...","t":"-","u":"..-","v":texts["...-"],"w":".--","x":texts["-..-"],"y":texts["-.--"],"z":texts["--.."]}
    text = " ".join(args).lower()
    result = " ".join(m.get(c,"?") for c in text if c != " ")
    return ftexts["📡 `{result}`"]



async def get_description():
    return {
        "ru": texts["Команда morse"],
        "en": texts["Command morse"],
        "ua": texts["Команда morse"]
    }
