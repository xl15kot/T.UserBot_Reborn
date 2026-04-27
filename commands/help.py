# help.py
import os

TEXTS = {
    "ru": {"title": "📖 Доступные команды", "total": "Всего команд", "tip": "💡 Свои команды добавляй в папку commands/"},
    "en": {"title": "📖 Available commands", "total": "Total commands", "tip": "💡 Add your commands to commands/ folder"},
    "ua": {"title": "📖 Доступні команди", "total": "Всього команд", "tip": "💡 Свої команди додавай до папки commands/"}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    
    cmds = []
    if os.path.exists("commands"):
        for f in os.listdir("commands"):
            if f.endswith(".py") and not f.startswith("__") and f != "help.py":
                cmd_name = f[:-3]
                cmds.append(f".{cmd_name}")
    
    cmds = sorted(cmds)
    
    result = f"{texts['title']}\n\n"
    result += "\n".join(cmds)
    result += f"\n\n━━━━━━━━━━━━━━━━━━━━━━\n📦 {texts['total']}: {len(cmds)}\n{texts['tip']}"
    
    return result