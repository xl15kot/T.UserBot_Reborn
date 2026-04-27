# md5.py
import hashlib
TEXTS = {"ru": "MD5 хэш", "en": "MD5 hash", "ua": "MD5 хэш", "usage": ".md5 <текст>"}
async def execute(event, args, client, db, LANG):
    if not args:
        return f"❌ {TEXTS['usage']}"
    return f"🔐 {TEXTS[LANG['lang_code']]}: {hashlib.md5(' '.join(args).encode()).hexdigest()}"
