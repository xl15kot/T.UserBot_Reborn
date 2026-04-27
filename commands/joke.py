# joke.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'Почему программисты не любят природу? Много багов! 🐛': 'Почему программисты не любят природу? Много багов! 🐛', 'Git push — и молись. 🙏': 'Git push — и молись. 🙏', 'Что говорит один бит другому? — Дай байт! 💾': 'Что говорит один бит другому? — Дай байт! 💾', 'Есть 10 типов людей: те, кто понимает бинарный код, и те, кто нет.': 'Есть 10 типов людей: те, кто понимает бинарный код, и те, кто нет.', 'try { любовь } catch(Exception e) { сон }': 'try { любовь } catch(Exception e) { сон }', '😂 {random.choice(jokes)}': '😂 {random.choice(jokes)}', 'Команда joke': 'Команда joke', 'Command joke': 'Command joke'}

# joke.py
#Ru: Команда joke
#En: Command joke
#Ua: Команда joke

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
    jokes = [
        texts["Почему программисты не любят природу? Много багов! 🐛"],
        texts["Git push — и молись. 🙏"],
        texts["Что говорит один бит другому? — Дай байт! 💾"],
        texts["Есть 10 типов людей: те, кто понимает бинарный код, и те, кто нет."],
        texts["try { любовь } catch(Exception e) { сон }"]
    ]
    return ftexts["😂 {random.choice(jokes)}"]



async def get_description():
    return {
        "ru": texts["Команда joke"],
        "en": texts["Command joke"],
        "ua": texts["Команда joke"]
    }
