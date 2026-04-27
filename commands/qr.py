# qr.py
TEXTS = {"ru": "QR код", "en": "QR code", "ua": "QR код", "usage": ".qr <текст>"}
async def execute(event, args, client, db, LANG):
    if not args:
        return f"❌ {TEXTS['usage']}"
    text = "+".join(args)
    return f"📱 {TEXTS[LANG['lang_code']]}: https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={text}"
