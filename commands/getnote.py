# getnote.py
#Ru: Показать заметку
#En: Show note
#Ua: Показати нотатку

TEXTS = {
    "ru": {"not_found": "❌ Заметка не найдена", "usage": "❌ .getnote <название>"},
    "en": {"not_found": "❌ Note not found", "usage": "❌ .getnote <name>"},
    "ua": {"not_found": "❌ Нотатку не знайдено", "usage": "❌ .getnote <назва>"}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    
    if not args:
        return texts["usage"]
    
    db.c.execute("SELECT content FROM notes WHERE user_id=? AND title=?", (event.sender_id, args[0]))
    note = db.c.fetchone()
    
    if note:
        return f"📄 **{args[0]}**\n\n{note[0]}"
    else:
        return texts["not_found"]