# sysinfo.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'Usage: .sysinfo <text>': 'Использование: .sysinfo <text>', 'Result: {text}': 'Результат: {text}'}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if not args:
        return texts["Usage: .sysinfo <text>"]
    
    text = " ".join(args)
    return ftexts["Result: {text}"]
