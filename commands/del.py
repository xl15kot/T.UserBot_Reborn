# del.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'Usage: .del <text>': 'Использование: .del <text>', 'Result: {text}': 'Результат: {text}'}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if not args:
        return texts["Usage: .del <text>"]
    
    text = " ".join(args)
    return ftexts["Result: {text}"]
