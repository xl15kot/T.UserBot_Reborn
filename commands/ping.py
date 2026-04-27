# ping.py
import time
TEXTS = {"ru": "Понг", "en": "Pong", "ua": "Понг"}
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    start = time.time()
    await event.edit("🏓")
    return f"🏓 {TEXTS[lang]}! {round((time.time()-start)*1000)}ms"
