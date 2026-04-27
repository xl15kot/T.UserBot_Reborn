# info.py
TEXTS = {
    "ru": {"not_found": "❌ Пользователь не найден", "name": "Имя", "id": "ID", "username": "Юзернейм", "none": "нет"},
    "en": {"not_found": "❌ User not found", "name": "Name", "id": "ID", "username": "Username", "none": "none"},
    "ua": {"not_found": "❌ Користувача не знайдено", "name": "Ім'я", "id": "ID", "username": "Юзернейм", "none": "немає"}
}
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if args:
        try:
            u = await client.get_entity(args[0])
            return f"👤 {texts['name']}: {u.first_name}\n🆔 {texts['id']}: {u.id}"
        except:
            return texts["not_found"]
    me = await client.get_me()
    return f"👤 {texts['name']}: {me.first_name}\n🆔 {texts['id']}: {me.id}"
