# hangman.py
#Ru: Игра виселица
#En: Hangman game
#Ua: Гра шибениця

import random

TEXTS = {
    "ru": {
        "start": "🪢 ВИСЕЛИЦА\n```\n{}\n```\nСлово: `{}`\n.hg <буква>",
        "hit": "✅ Есть буква '{}'!\n```\n{}\n```\n`{}`",
        "miss": "❌ Нет '{}' (попыток: {})\n```\n{}\n```\n`{}`",
        "win": "🎉 ПОБЕДА!\nСлово: {}",
        "lose": "💀 ПРОИГРЫШ\n```\n{}\n```\nСлово: {}",
        "no_game": "❌ .hangman — начать",
        "already": "⚠️ Буква '{}' уже угадана"
    },
    "en": {
        "start": "🪢 HANGMAN\n```\n{}\n```\nWord: `{}`\n.hg <letter>",
        "hit": "✅ Letter '{}' found!\n```\n{}\n```\n`{}`",
        "miss": "❌ No '{}' (attempts left: {})\n```\n{}\n```\n`{}`",
        "win": "🎉 VICTORY!\nWord: {}",
        "lose": "💀 GAME OVER\n```\n{}\n```\nWord: {}",
        "no_game": "❌ Start: .hangman",
        "already": "⚠️ Letter '{}' already guessed"
    },
    "ua": {
        "start": "🪢 ШИБЕНИЦЯ\n```\n{}\n```\nСлово: `{}`\n.hg <буква>",
        "hit": "✅ Є буква '{}'!\n```\n{}\n```\n`{}`",
        "miss": "❌ Немає '{}' (спроб залишилось: {})\n```\n{}\n```\n`{}`",
        "win": "🎉 ПЕРЕМОГА!\nСлово: {}",
        "lose": "💀 ПОРАЗКА\n```\n{}\n```\nСлово: {}",
        "no_game": "❌ .hangman — почати",
        "already": "⚠️ Буква '{}' вже вгадана"
    }
}

hangman_games = {}

def hangman_pic(wrong):
    stages = [
        "  ___\n |   |\n |\n |\n |\n_|_",
        "  ___\n |   |\n |   😐\n |\n |\n_|_",
        "  ___\n |   |\n |   😐\n |   |\n |\n_|_",
        "  ___\n |   |\n |   😐\n |  /|\n |\n_|_",
        "  ___\n |   |\n |   😐\n |  /|\\\n |\n_|_",
        "  ___\n |   |\n |   😐\n |  /|\\\n |  /\n_|_",
        "  ___\n |   |\n |   😵\n |  /|\\\n |  / \\\n_|_"
    ]
    return stages[min(wrong, 6)]

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    uid = event.sender_id
    words = ["python", "telegram", "userbot", "программа", "компьютер"]
    
    if not args:
        word = random.choice(words)
        hangman_games[uid] = {"word": word, "guessed": set(), "wrong": 0}
        disp = " ".join("_" for _ in word)
        return texts["start"].format(hangman_pic(0), disp)
    
    if uid not in hangman_games:
        return texts["no_game"]
    
    g = hangman_games[uid]
    letter = args[0].lower()
    
    if letter in g["guessed"]:
        return texts["already"].format(letter)
    
    g["guessed"].add(letter)
    
    if letter in g["word"]:
        disp = " ".join(ch if ch in g["guessed"] else "_" for ch in g["word"])
        if "_" not in disp:
            del hangman_games[uid]
            return texts["win"].format(g["word"])
        return texts["hit"].format(letter, hangman_pic(g["wrong"]), disp)
    else:
        g["wrong"] += 1
        disp = " ".join(ch if ch in g["guessed"] else "_" for ch in g["word"])
        if g["wrong"] >= 6:
            word = g["word"]
            del hangman_games[uid]
            return texts["lose"].format(hangman_pic(6), word)
        return texts["miss"].format(letter, 6 - g["wrong"], hangman_pic(g["wrong"]), disp)