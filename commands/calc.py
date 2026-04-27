# calc.py
TEXTS = {"ru": "Результат", "en": "Result", "ua": "Результат", "error": "Ошибка", "usage": ".calc <выражение>"}
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    if not args:
        return f"❌ {TEXTS['usage']}"
    try:
        result = eval(" ".join(args))
        return f"🧮 {TEXTS[lang]}: {result}"
    except:
        return f"❌ {TEXTS['error']}"
