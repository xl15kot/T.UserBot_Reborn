# todos.py
#Ru: Список задач
#En: Todo list
#Ua: Список завдань

TEXTS = {
    "ru": {"title": "📋 Список задач:", "empty": "📭 У вас нет задач", "done": "✅", "pending": "⬜"},
    "en": {"title": "📋 Todo list:", "empty": "📭 You have no tasks", "done": "✅", "pending": "⬜"},
    "ua": {"title": "📋 Список завдань:", "empty": "📭 У вас немає завдань", "done": "✅", "pending": "⬜"}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    
    db.c.execute("SELECT id, task, done FROM todos WHERE user_id=? ORDER BY done, id", (event.sender_id,))
    todos = db.c.fetchall()
    
    if not todos:
        return texts["empty"]
    
    result = f"{texts['title']}\n"
    for tid, task, done in todos:
        status = texts["done"] if done else texts["pending"]
        result += f"{status} #{tid}: {task}\n"
    
    return result