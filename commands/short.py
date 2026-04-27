# short.py
import requests
TEXTS = {"ru": "Короткая ссылка", "en": "Short URL", "ua": "Коротке посилання", "error": "Ошибка", "usage": ".short <url>"}
async def execute(event, args, client, db, LANG):
    if not args:
        return f"❌ {TEXTS['usage']}"
    try:
        r = requests.get(f"https://tinyurl.com/api-create.php?url={args[0]}", timeout=10)
        if r.status_code == 200:
            return f"🔗 {TEXTS[LANG['lang_code']]}: {r.text}"
    except:
        pass
    return f"❌ {TEXTS['error']}"
