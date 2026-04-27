# 8ball.py
import random
TEXTS = {
    "ru": {"q": "Вопрос", "a": "Ответ", "yes": "✅ Определённо да", "no": "❌ Нет", "maybe": "🤔 Возможно", "def": "🌟 Конечно", "usage": ".8ball <вопрос>"},
    "en": {"q": "Question", "a": "Answer", "yes": "✅ Definitely yes", "no": "❌ No", "maybe": "🤔 Maybe", "def": "🌟 Of course", "usage": ".8ball <question>"},
    "ua": {"q": "Питання", "a": "Відповідь", "yes": "✅ Так", "no": "❌ Ні", "maybe": "🤔 Можливо", "def": "🌟 Звичайно", "usage": ".8ball <питання>"}
}
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    if not args:
        return f"❌ {texts['usage']}"
    answers = [texts["yes"], texts["no"], texts["maybe"], texts["def"]]
    return f"🎱 {texts['q']}: {' '.join(args)}\n\n{texts['a']}: {random.choice(answers)}"
