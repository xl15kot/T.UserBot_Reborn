# os.py
#Ru: Description in Russian
#En: Description in English
#Ua: Description in Ukrainian

TEXTS = {'lang_code': 'lang_code', 'Windows': 'Windows', 'Linux': 'Linux', '/etc/os-release': '/etc/os-release', 'PRETTY_NAME=': 'PRETTY_NAME=', 'Darwin': 'Darwin', 'macOS': 'macOS', '{icon} **{os_type}**\\n': '{icon} **{os_type}**\\n', '🖥 **OS:** {os_type}': '🖥 **OS:** {os_type}', '📀 **Kernel:** {platform.release()}': '📀 **Kernel:** {platform.release()}', '⚙️ **Arch:** {platform.machine()}': '⚙️ **Arch:** {platform.machine()}', '🌐 **Host:** {socket.gethostname()}': '🌐 **Host:** {socket.gethostname()}', '🐍 **Python:** {platform.python_version()}': '🐍 **Python:** {platform.python_version()}', ' @ {cpu_freq.current:.0f} MHz': ' @ {cpu_freq.current:.0f} MHz', '🔲 **CPU:** {cores}C/{threads}T{freq_str} | Load: {cpu_load}%': '🔲 **CPU:** {cores}C/{threads}T{freq_str} | Load: {cpu_load}%', '💾 **RAM:** {ram.used//1024**2} / {ram.total//1024**2} MB ({ram.percent}%)': '💾 **RAM:** {ram.used//1024**2} / {ram.total//1024**2} MB ({ram.percent}%)', '⏱ **Uptime:** {up//3600}h {(up%3600)//60}m': '⏱ **Uptime:** {up//3600}h {(up%3600)//60}m', 'C:\\\\" if os_name == ': 'C:\\\\" if os_name == ', ' else ': ' else ', '\n        try:\n            d = psutil.disk_usage(mount)\n            lines.append(f': '\n        try:\n            d = psutil.disk_usage(mount)\n            lines.append(f', ')\n        except Exception:\n            pass\n\n    except ImportError:\n        lines.append(': ')\n        except Exception:\n            pass\n\n    except ImportОшибка:\n        lines.append(', ')\n\n    return ': ')\n\n    return ', '.join(lines)\n\n\n\nasync def get_description():\n    return {\n        ': '.join(lines)\n\n\n\nasync def get_description():\n    return {\n        ', ',\n        ': ',\n        '}

# os.py
#Ru: Команда os
#En: Command os
#Ua: Команда os

import random
import asyncio

# Мультиязычные тексты для этой команды
TEXTS = {
    "ru": {'\\n': '\\n'},
    "en": {'\\n': '\\n'},
    "ua": {'\\n': '\\n'}
}

async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    lang = LANG[texts["lang_code"]]
    texts = TEXTS[lang]
    
async def execute(event, args, client, db, LANG):
    lang = LANG["lang_code"]
    texts = TEXTS[lang]
    os_name = platform.system()

    if os_name == texts["Windows"]:
        icon, os_type = "🪟", texts["Windows"]
    elif os_name == texts["Linux"]:
        icon, os_type = "🐧", texts["Linux"]
        try:
            with open(texts["/etc/os-release"]) as f:
                for line in f:
                    if line.startswith(texts["PRETTY_NAME="]):
                        os_type = line.split("=", 1)[1].strip().strip('"')
                        break
        except Exception:
            pass
    elif os_name == texts["Darwin"]:
        icon, os_type = "🍎", texts["macOS"]
    else:
        icon, os_type = "💻", os_name

    lines = [ftexts["{icon} **{os_type}**\n"]]

    # OS
    lines.append(ftexts["🖥 **OS:** {os_type}"])
    lines.append(ftexts["📀 **Kernel:** {platform.release()}"])
    lines.append(ftexts["⚙️ **Arch:** {platform.machine()}"])
    lines.append(ftexts["🌐 **Host:** {socket.gethostname()}"])
    lines.append(ftexts["🐍 **Python:** {platform.python_version()}"])

    # CPU + RAM через psutil если есть
    try:
        import psutil

        # CPU
        cpu_freq = psutil.cpu_freq()
        freq_str = ftexts[" @ {cpu_freq.current:.0f} MHz"] if cpu_freq else ""
        cores   = psutil.cpu_count(logical=False)
        threads = psutil.cpu_count(logical=True)
        cpu_load = psutil.cpu_percent(interval=0.3)
        lines.append(ftexts["🔲 **CPU:** {cores}C/{threads}T{freq_str} | Load: {cpu_load}%"])

        # RAM
        ram = psutil.virtual_memory()
        lines.append(ftexts["💾 **RAM:** {ram.used//1024**2} / {ram.total//1024**2} MB ({ram.percent}%)"])

        # Uptime
        up = int(time.time() - psutil.boot_time())
        lines.append(ftexts["⏱ **Uptime:** {up//3600}h {(up%3600)//60}m"])

        # Disk (только root / C:\)
        mount = "C:\\" if os_name == texts["Windows"] else "/"
        try:
            d = psutil.disk_usage(mount)
            lines.append(f"💿 **Disk [{mount}]:** {d.used/1024**3:.1f} / {d.total/1024**3:.1f} GB ({d.percent}%)")
        except Exception:
            pass

    except ImportError:
        lines.append("_(установи psutil для CPU/RAM: pip install psutil)_")

    return "\n".join(lines)



async def get_description():
    return {
        "ru": "Команда os",
        "en": "Command os",
        "ua": "Команда os"
    }
