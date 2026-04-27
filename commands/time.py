# time.py
import time
TEXTS = {"ru": "🕐 Время", "en": "🕐 Time", "ua": "🕐 Час"}
async def execute(event, args, client, db, LANG):
    return f"{TEXTS[LANG['lang_code']]}: {time.strftime('%H:%M:%S')}"
