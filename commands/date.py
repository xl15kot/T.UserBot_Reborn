# date.py
import time
TEXTS = {"ru": "📅 Дата", "en": "📅 Date", "ua": "📅 Дата"}
async def execute(event, args, client, db, LANG):
    return f"{TEXTS[LANG['lang_code']]}: {time.strftime('%d.%m.%Y')}"
