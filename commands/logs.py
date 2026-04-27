# logs.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', '📋 **ПОСЛЕДНИЕ ЛОГИ**\\n```\\n{logs}\\n```': '📋 **ПОСЛЕДНИЕ ЛОГИ**\\n```\\n{logs}\\n```', 'Команда logs': 'Команда logs', 'Command logs': 'Command logs'}

# logs.py
#Ru: Команда logs
#En: Command logs
#Ua: Команда logs

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
    from main import log_messages
    logs = "\n".join(log_messages[-30:])
    return ftexts["📋 **ПОСЛЕДНИЕ ЛОГИ**\n```\n{logs}\n```"]


async def get_description():
    return {
        "ru": texts["Команда logs"],
        "en": texts["Command logs"],
        "ua": texts["Команда logs"]
    }
