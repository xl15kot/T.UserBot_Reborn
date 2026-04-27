# notes.py
#Ru: Список заметок
#En: Notes list
#Ua: Список нотаток

TEXTS = {
    "ru": {"title": "📝 Ваши заметки:", "empty": "📭 У вас нет заметок"},
    "en": {"title": "📝 Your notes:", "empty": "📭 You have no notes"},
    "ua": {"title": "📝 Ваші нотатки:", "empty": "📭 У вас немає нотаток"}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    
    db.c.execute("SELECT title, created FROM notes WHERE user_id=? ORDER BY created DESC LIMIT 10", (event.sender_id,))
    notes = db.c.fetchall()
    
    if not notes:
        return texts["empty"]
    
    result = f"{texts['title']}\n"
    for title, created in notes:
        result += f"• {title}\n"
    
    return result