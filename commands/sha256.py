# sha256.py
import hashlib
TEXTS = {"ru": "SHA256 хэш", "en": "SHA256 hash", "ua": "SHA256 хэш", "usage": ".sha256 <текст>"}
async def execute(event, args, client, db, LANG):
    if not args:
        return f"❌ {TEXTS['usage']}"
    return f"🔐 {TEXTS[LANG['lang_code']]}: {hashlib.sha256(' '.join(args).encode()).hexdigest()}"
