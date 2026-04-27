# flip.py
TEXTS = {"ru": "Результат", "en": "Result", "ua": "Результат", "usage": ".flip <текст>"}
async def execute(event, args, client, db, LANG):
    if not args:
        return f"❌ {TEXTS['usage']}"
    return f"🔄 {TEXTS[LANG['lang_code']]}: {' '.join(args)[::-1]}"
