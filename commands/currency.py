# currency.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {' .currency <сумма> <из> <в>': ' .currency <сумма> <из> <в>', ' Неизвестная пара. Поддержка: USD/RUB/EUR': ' Неизвестная пара. Поддержка: USD/RUB/EUR', 'lang_code': 'lang_code', '❌ .currency <сумма> <из> <в>': '❌ .currency <сумма> <из> <в>', '💱 {amt} {fr} = {amt*rates[key]:.2f} {to}': '💱 {amt} {fr} = {amt*rates[key]:.2f} {to}', '❌ Неизвестная пара. Поддержка: USD/RUB/EUR': '❌ Неизвестная пара. Поддержка: USD/RUB/EUR', 'Команда currency': 'Команда currency', 'Command currency': 'Command currency'}

# currency.py
#Ru: Команда currency
#En: Command currency
#Ua: Команда currency

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {' .currency <сумма> <из> <в>': ' .currency <сумма> <из> <в>', ' Неизвестная пара. Поддержка: USD/RUB/EUR': ' Неизвестная пара. Поддержка: USD/RUB/EUR'},
    "en": {' .currency <сумма> <из> <в>': ' .currency <сумма> <из> <в>', ' Неизвестная пара. Поддержка: USD/RUB/EUR': ' Неизвестная пара. Поддержка: USD/RUB/EUR'},
    "ua": {' .currency <сумма> <из> <в>': ' .currency <сумма> <из> <в>', ' Неизвестная пара. Поддержка: USD/RUB/EUR': ' Неизвестная пара. Поддержка: USD/RUB/EUR'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if len(args) < 3:
        return texts["❌ .currency <сумма> <из> <в>"]
    try:
        amt = float(args[0])
        rates = {("USD","RUB"): 92, ("RUB","USD"): 0.0109, ("EUR","RUB"): 99.5}
        fr, to = args[1].upper(), args[2].upper()
        key = (fr, to)
        if key in rates:
            return ftexts["💱 {amt} {fr} = {amt*rates[key]:.2f} {to}"]
        else:
            return texts["❌ Неизвестная пара. Поддержка: USD/RUB/EUR"]
    except:
        return texts["❌ .currency <сумма> <из> <в>"]



async def get_description():
    return {
        "ru": texts["Команда currency"],
        "en": texts["Command currency"],
        "ua": texts["Команда currency"]
    }
