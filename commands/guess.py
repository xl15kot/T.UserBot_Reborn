# guess.py
import random
TEXTS = {
    "ru": {"start": "🎯 Загадал число от 1 до 100\n.guess <число>", "higher": "📈 Больше!", "lower": "📉 Меньше!", "win": "🎉 Правильно! Число было {}", "invalid": "❌ Введите число", "no_game": "❌ Начните: .guess"},
    "en": {"start": "🎯 I'm thinking of a number from 1 to 100\n.guess <number>", "higher": "📈 Higher!", "lower": "📉 Lower!", "win": "🎉 Correct! The number was {}", "invalid": "❌ Enter a number", "no_game": "❌ Start with: .guess"},
    "ua": {"start": "🎯 Загадав число від 1 до 100\n.guess <число>", "higher": "📈 Більше!", "lower": "📉 Менше!", "win": "🎉 Правильно! Число було {}", "invalid": "❌ Введіть число", "no_game": "❌ Почніть: .guess"}
}
guess_numbers = {}
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    uid = event.sender_id
    if not args:
        guess_numbers[uid] = random.randint(1, 100)
        return texts["start"]
    if args[0].isdigit():
        if uid not in guess_numbers:
            return texts["no_game"]
        g = int(args[0])
        n = guess_numbers[uid]
        if g < n:
            return texts["higher"]
        elif g > n:
            return texts["lower"]
        else:
            del guess_numbers[uid]
            return texts["win"].format(n)
    return texts["invalid"]
