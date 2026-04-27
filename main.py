#0.3
import os
import sys
import json
import time
import asyncio
import threading
import sqlite3
import importlib.util
import random
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

VERSION = "v0.3 beta"
TEAM = "TeaDevs"

LANGUAGES = {
    "ru": {
        "app_title": f"T.UserBot Reborn {VERSION}",
        "commands_btn": "📋 Команды",
        "start": "▶ СТАРТ",
        "stop": "■ СТОП",
        "api_settings": "🔑 API",
        "settings": "⚙️ Настройки",
        "exit": "✖ Выход",
        "online": "● ОНЛАЙН",
        "offline": "● ОФФЛАЙН",
        "bot_started": "Бот запущен",
        "bot_stopped": "Бот остановлен",
        "api_saved": "API сохранён",
        "settings_saved": "Настройки сохранены",
        "commands_loaded": "команд загружено",
        "no_api": "Нет API данных",
        "unknown_cmd": "Неизвестная команда",
        "tab_general": "Основные",
        "tab_appearance": "Внешний вид",
        "tab_bot": "Бот",
        "tab_console": "Консоль",
        "tab_about": "О программе",
        "language": "Язык",
        "russian": "Русский",
        "english": "English",
        "ukrainian": "Українська",
        "autostart": "Автозапуск бота",
        "theme": "Тема",
        "dark": "Тёмная",
        "light": "Светлая",
        "command_prefix": "Префикс команд",
        "default_prefix": "Точка (.)",
        "total_commands": "Всего команд",
        "auth_title": "Авторизация Telegram",
        "auth_code": "Код подтверждения",
        "auth_code_sent": "Код отправлен в Telegram",
        "auth_submit": "Подтвердить",
        "auth_success": "Авторизация успешна!",
        "auth_invalid_code": "Неверный код",
        "auth_connecting": "Подключение к Telegram...",
        "auth_waiting": "Ожидание авторизации...",
        "auth_2fa_title": "Двухфакторная аутентификация",
        "auth_2fa_info": "Введите пароль двухфакторной аутентификации",
        "save": "Сохранить",
        "cancel": "Отмена",
        "reset": "Сбросить",
        "telegram_api": "TELEGRAM API",
        "api_id": "API ID",
        "api_hash": "API HASH",
        "phone": "НОМЕР ТЕЛЕФОНА",
        "phone_format": "Формат: +79001234567",
        "export_logs": "Экспорт логов",
        "about_text": f"T.UserBot Reborn {VERSION}\n\nРазработчики: AveBas, LimuxMintREAL\nСтудия: TeaDevs\n\n© 2026 TeaDevs",
        "restart": "Перезапуск",
        "restart_question": "Перезапустить приложение?",
        "error": "Ошибка",
        "api_id_error": "API ID должен быть числом!",
        "api_hash_error": "Введите API Hash!",
        "phone_error": "Введите номер телефона!",
        "logs_saved": "Логи сохранены",
        "clear": "Очистить",
        "export": "Экспорт",
        "nav_console": "Консоль",
        "nav_commands": "Команды",
        "nav_stats": "Статистика",
        "nav_settings": "Настройки",
        "nav_about": "О программе",
        "nav_editor": "Редактор",
        "cmd_name": "Команда",
        "cmd_calls": "Вызовов",
        "cmd_status": "Статус",
        "cmd_reload": "Перезагрузить",
        "cmd_active": "Активна",
        "stats_title": "Статистика вызовов команд",
        "stats_no_data": "Нет данных",
        "tray_show": "Показать",
        "tray_hide": "Скрыть",
        "tray_quit": "Выход",
        "tray_minimized": "T.UserBot свёрнут в трей",
        "tray_bot_started": "Бот запущен!",
        "tray_bot_stopped": "Бот остановлен",
        "minimize_to_tray": "Сворачивать в трей",
        "first_run_title": "Первый запуск",
        "first_run_subtitle": "Первоначальная настройка",
        "first_run_save": "Сохранить и продолжить",
        "first_run_exit": "Выход",
        "lang_group": "Язык / Language / Мова",
        "loading": "Загрузка...",
        "preparing": "Подготовка...",
        "done": "Готово!",
        "create_command": "Создать команду",
        "command_name": "Название команды:",
        "command_code": "Код команды:",
        "create": "Создать",
        "delete": "Удалить",
        "save_code": "Сохранить",
        "code_editor": "Редактор кода",
        "select_command": "Выберите команду",
    },
    "en": {
        "app_title": f"T.UserBot Reborn {VERSION}",
        "commands_btn": "📋 Commands",
        "start": "▶ START",
        "stop": "■ STOP",
        "api_settings": "🔑 API",
        "settings": "⚙️ Settings",
        "exit": "✖ Exit",
        "online": "● ONLINE",
        "offline": "● OFFLINE",
        "bot_started": "Bot started",
        "bot_stopped": "Bot stopped",
        "api_saved": "API saved",
        "settings_saved": "Settings saved",
        "commands_loaded": "commands loaded",
        "no_api": "No API data",
        "unknown_cmd": "Unknown command",
        "tab_general": "General",
        "tab_appearance": "Appearance",
        "tab_bot": "Bot",
        "tab_console": "Console",
        "tab_about": "About",
        "language": "Language",
        "russian": "Russian",
        "english": "English",
        "ukrainian": "Ukrainian",
        "autostart": "Auto-start bot",
        "theme": "Theme",
        "dark": "Dark",
        "light": "Light",
        "command_prefix": "Command prefix",
        "default_prefix": "Dot (.)",
        "total_commands": "Total commands",
        "auth_title": "Telegram Authorization",
        "auth_code": "Confirmation code",
        "auth_code_sent": "Code sent to Telegram",
        "auth_submit": "Submit",
        "auth_success": "Authorization successful!",
        "auth_invalid_code": "Invalid code",
        "auth_connecting": "Connecting to Telegram...",
        "auth_waiting": "Waiting for authorization...",
        "auth_2fa_title": "Two-Factor Authentication",
        "auth_2fa_info": "Enter your two-factor authentication password",
        "save": "Save",
        "cancel": "Cancel",
        "reset": "Reset",
        "telegram_api": "TELEGRAM API",
        "api_id": "API ID",
        "api_hash": "API HASH",
        "phone": "PHONE NUMBER",
        "phone_format": "Format: +79001234567",
        "export_logs": "Export logs",
        "about_text": f"T.UserBot Reborn {VERSION}\n\nDevelopers: AveBas, LimuxMintREAL\nStudio: TeaDevs\n\n© 2026 TeaDevs",
        "restart": "Restart",
        "restart_question": "Restart the application?",
        "error": "Error",
        "api_id_error": "API ID must be a number!",
        "api_hash_error": "Enter API Hash!",
        "phone_error": "Enter phone number!",
        "logs_saved": "Logs saved",
        "clear": "Clear",
        "export": "Export",
        "nav_console": "Console",
        "nav_commands": "Commands",
        "nav_stats": "Statistics",
        "nav_settings": "Settings",
        "nav_about": "About",
        "nav_editor": "Editor",
        "cmd_name": "Command",
        "cmd_calls": "Calls",
        "cmd_status": "Status",
        "cmd_reload": "Reload",
        "cmd_active": "Active",
        "stats_title": "Command Call Statistics",
        "stats_no_data": "No data",
        "tray_show": "Show",
        "tray_hide": "Hide",
        "tray_quit": "Quit",
        "tray_minimized": "T.UserBot minimized to tray",
        "tray_bot_started": "Bot started!",
        "tray_bot_stopped": "Bot stopped",
        "minimize_to_tray": "Minimize to tray",
        "first_run_title": "First Launch",
        "first_run_subtitle": "Initial setup",
        "first_run_save": "Save and continue",
        "first_run_exit": "Exit",
        "lang_group": "Language",
        "loading": "Loading...",
        "preparing": "Preparing...",
        "done": "Done!",
        "create_command": "Create command",
        "command_name": "Command name:",
        "command_code": "Command code:",
        "create": "Create",
        "delete": "Delete",
        "save_code": "Save",
        "code_editor": "Code editor",
        "select_command": "Select a command",
    },
    "ua": {
        "app_title": f"T.UserBot Reborn {VERSION}",
        "commands_btn": "📋 Команди",
        "start": "▶ СТАРТ",
        "stop": "■ СТОП",
        "api_settings": "🔑 API",
        "settings": "⚙️ Налаштування",
        "exit": "✖ Вихід",
        "online": "● ОНЛАЙН",
        "offline": "● ОФЛАЙН",
        "bot_started": "Бот запущено",
        "bot_stopped": "Бот зупинено",
        "api_saved": "API збережено",
        "settings_saved": "Налаштування збережено",
        "commands_loaded": "команд завантажено",
        "no_api": "Немає даних API",
        "unknown_cmd": "Невідома команда",
        "tab_general": "Основні",
        "tab_appearance": "Зовнішній вигляд",
        "tab_bot": "Бот",
        "tab_console": "Консоль",
        "tab_about": "Про програму",
        "language": "Мова",
        "russian": "Російська",
        "english": "Англійська",
        "ukrainian": "Українська",
        "autostart": "Автозапуск бота",
        "theme": "Тема",
        "dark": "Темна",
        "light": "Світла",
        "command_prefix": "Префікс команд",
        "default_prefix": "Крапка (.)",
        "total_commands": "Всього команд",
        "auth_title": "Авторизація Telegram",
        "auth_code": "Код підтвердження",
        "auth_code_sent": "Код надіслано в Telegram",
        "auth_submit": "Підтвердити",
        "auth_success": "Авторизація успішна!",
        "auth_invalid_code": "Невірний код",
        "auth_connecting": "Підключення до Telegram...",
        "auth_waiting": "Очікування авторизації...",
        "auth_2fa_title": "Двофакторна автентифікація",
        "auth_2fa_info": "Введіть пароль двофакторної автентифікації",
        "save": "Зберегти",
        "cancel": "Скасувати",
        "reset": "Скинути",
        "telegram_api": "TELEGRAM API",
        "api_id": "API ID",
        "api_hash": "API HASH",
        "phone": "НОМЕР ТЕЛЕФОНУ",
        "phone_format": "Формат: +79001234567",
        "export_logs": "Експорт логів",
        "about_text": f"T.UserBot Reborn {VERSION}\n\nРозробники: AveBas, LimuxMintREAL\nСтудія: TeaDevs\n\n© 2026 TeaDevs",
        "restart": "Перезапуск",
        "restart_question": "Перезапустити застосунок?",
        "error": "Помилка",
        "api_id_error": "API ID має бути числом!",
        "api_hash_error": "Введіть API Hash!",
        "phone_error": "Введіть номер телефону!",
        "logs_saved": "Логи збережено",
        "clear": "Очистити",
        "export": "Експорт",
        "nav_console": "Консоль",
        "nav_commands": "Команди",
        "nav_stats": "Статистика",
        "nav_settings": "Налаштування",
        "nav_about": "Про програму",
        "nav_editor": "Редактор",
        "cmd_name": "Команда",
        "cmd_calls": "Викликів",
        "cmd_status": "Статус",
        "cmd_reload": "Перезавантажити",
        "cmd_active": "Активна",
        "stats_title": "Статистика викликів команд",
        "stats_no_data": "Немає даних",
        "tray_show": "Показати",
        "tray_hide": "Приховати",
        "tray_quit": "Вихід",
        "tray_minimized": "T.UserBot згорнуто в трей",
        "tray_bot_started": "Бот запущено!",
        "tray_bot_stopped": "Бот зупинено",
        "minimize_to_tray": "Згортати в трей",
        "first_run_title": "Перший запуск",
        "first_run_subtitle": "Початкове налаштування",
        "first_run_save": "Зберегти і продовжити",
        "first_run_exit": "Вихід",
        "lang_group": "Мова",
        "loading": "Завантаження...",
        "preparing": "Підготовка...",
        "done": "Готово!",
        "create_command": "Створити команду",
        "command_name": "Назва команди:",
        "command_code": "Код команди:",
        "create": "Створити",
        "delete": "Видалити",
        "save_code": "Зберегти",
        "code_editor": "Редактор коду",
        "select_command": "Виберіть команду",
    }
}

THEMES = {
    "dark": {
        "name": "Dark", "bg": "#0D1117", "bg2": "#161B22", "bg3": "#21262D",
        "fg": "#C9D1D9", "fg2": "#8B949E", "accent": "#238636", "accent_hover": "#2EA043",
        "danger": "#DA3633", "border": "#30363D", "console_bg": "#0D1117",
        "console_fg": "#C9D1D9", "title_bg": "#161B22", "nav_bg": "#0D1117",
        "nav_hover": "#161B22", "nav_active": "#1F6FEB22", "nav_active_border": "#238636",
        "success": "#3FB950", "warning": "#D29922", "error_color": "#F85149",
        "info": "#58A6FF", "chart_bar": "#238636", "chart_bar2": "#1F6FEB", "chart_grid": "#21262D",
    },
    "light": {
        "name": "Light", "bg": "#FFFFFF", "bg2": "#F6F8FA", "bg3": "#E9ECEF",
        "fg": "#1F2328", "fg2": "#656D76", "accent": "#0969DA", "accent_hover": "#218BFF",
        "danger": "#CF222E", "border": "#D0D7DE", "console_bg": "#F6F8FA",
        "console_fg": "#1F2328", "title_bg": "#F6F8FA", "nav_bg": "#F6F8FA",
        "nav_hover": "#E9ECEF", "nav_active": "#0969DA22", "nav_active_border": "#0969DA",
        "success": "#1A7F37", "warning": "#9A6700", "error_color": "#CF222E",
        "info": "#0969DA", "chart_bar": "#0969DA", "chart_bar2": "#8250DF", "chart_grid": "#E9ECEF",
    },
}

default_settings = {
    "language": "ru", "theme": "dark", "autostart": False, "command_prefix": ".",
    "console_lines": 100, "console_font": "Consolas", "timestamps": True,
    "colored_output": True, "minimize_to_tray": True,
}

settings = default_settings.copy()
os.makedirs("data", exist_ok=True)
os.makedirs("commands", exist_ok=True)

def load_settings():
    global settings
    if os.path.exists("data/settings.json"):
        try:
            with open("data/settings.json", "r") as f:
                saved = json.load(f)
                settings.update(saved)
        except:
            pass

def save_settings():
    with open("data/settings.json", "w") as f:
        json.dump(settings, f, indent=2)

load_settings()

if settings.get("language") not in LANGUAGES:
    settings["language"] = "ru"

LANG = LANGUAGES[settings["language"]]
LANG["lang_code"] = settings["language"]
THEME = THEMES[settings["theme"]]

def load_app_icon(size=None):
    icon_paths = ["ico.png", "images/ico.png", "icon.png"]
    for path in icon_paths:
        if os.path.exists(path):
            try:
                pixmap = QPixmap(path)
                if size:
                    pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                return QIcon(pixmap), pixmap
            except:
                pass
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setFont(QFont("Segoe UI", 32))
    painter.setPen(QColor(THEME["accent"]))
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "🍵")
    painter.end()
    if size:
        pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return QIcon(pixmap), pixmap

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("data/userbot.db", check_same_thread=False)
        self.c = self.conn.cursor()
        self._init()
    def _init(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS economy (user_id INTEGER PRIMARY KEY, balance INTEGER DEFAULT 100, bank INTEGER DEFAULT 0, job TEXT DEFAULT 'Безработный', xp INTEGER DEFAULT 0, level INTEGER DEFAULT 1, last_work TEXT, last_daily TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS cmd_stats (cmd TEXT PRIMARY KEY, count INTEGER DEFAULT 0)")
        self.conn.commit()
    def stat(self, cmd):
        self.c.execute("INSERT INTO cmd_stats(cmd,count) VALUES(?,1) ON CONFLICT(cmd) DO UPDATE SET count=count+1", (cmd,))
        self.conn.commit()
    def get_all_stats(self):
        self.c.execute("SELECT cmd, count FROM cmd_stats ORDER BY count DESC")
        return self.c.fetchall()
    def get_cmd_count(self, cmd):
        self.c.execute("SELECT count FROM cmd_stats WHERE cmd=?", (cmd,))
        row = self.c.fetchone()
        return row[0] if row else 0

db = Database()

def load_api():
    if os.path.exists("data/api_data.json"):
        try:
            with open("data/api_data.json", "r") as f:
                d = json.load(f)
                return d.get("api_id"), d.get("api_hash"), d.get("phone")
        except:
            return None, None, None
    return None, None, None

def save_api(api_id, api_hash, phone):
    with open("data/api_data.json", "w") as f:
        json.dump({"api_id": api_id, "api_hash": api_hash, "phone": phone}, f, indent=2)

bot_client = None
bot_running = False
log_messages = []

def add_log(msg, msg_type="default"):
    timestamp = time.strftime('%H:%M:%S') if settings["timestamps"] else ""
    prefix = f"[{timestamp}] " if timestamp else ""
    log_messages.append((f"{prefix}{msg}", msg_type))
    if len(log_messages) > settings["console_lines"]:
        log_messages.pop(0)

def load_commands():
    commands = {}
    if not os.path.exists("commands"):
        return commands
    for file in os.listdir("commands"):
        if file.endswith(".py") and file != "__init__.py":
            cmd_name = file[:-3]
            file_path = os.path.join("commands", file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                spec = importlib.util.spec_from_file_location(cmd_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "execute"):
                    commands[cmd_name] = module.execute
                    add_log(f"  .{cmd_name}", "success")
            except Exception as e:
                add_log(f"  {file}: {e}", "error")
    return commands

def make_dialog_style():
    return (f"QDialog {{ background-color: {THEME['bg']}; }}"
            f"QLabel {{ color: {THEME['fg']}; }}"
            f"QLineEdit {{ background-color: {THEME['bg3']}; border: 1px solid {THEME['border']}; border-radius: 6px; padding: 6px; color: {THEME['fg']}; }}"
            f"QPushButton {{ background-color: {THEME['bg3']}; border: none; padding: 8px 16px; border-radius: 6px; color: {THEME['fg']}; }}"
            f"QPushButton:hover {{ background-color: {THEME['accent_hover']}; color: white; }}")

class StatsChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = []
        self.setMinimumHeight(200)
    def set_data(self, data):
        self.data = data[:15]
        self.setMinimumHeight(max(200, len(self.data) * 36 + 60))
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w = self.width()
        h = self.height()
        painter.fillRect(self.rect(), QColor(THEME["bg2"]))
        if not self.data:
            painter.setPen(QColor(THEME["fg2"]))
            painter.setFont(QFont("Segoe UI", 12))
            painter.drawText(self.rect(), Qt.AlignCenter, LANG["stats_no_data"])
            painter.end()
            return
        painter.setPen(QColor(THEME["fg"]))
        painter.setFont(QFont("Segoe UI", 11, QFont.Bold))
        painter.drawText(12, 24, LANG["stats_title"])
        max_val = max(v for _, v in self.data) if self.data else 1
        if max_val == 0:
            max_val = 1
        bar_area_left = 120
        bar_area_right = w - 60
        bar_area_width = bar_area_right - bar_area_left
        bar_height = 22
        y_start = 44
        spacing = 32
        colors = [QColor(THEME["chart_bar"]), QColor(THEME["chart_bar2"])]
        for i, (cmd, count) in enumerate(self.data):
            y = y_start + i * spacing
            color = colors[i % 2]
            painter.setPen(QColor(THEME["fg"]))
            painter.setFont(QFont("Consolas", 9))
            painter.drawText(8, y + 16, f".{cmd}")
            bar_w = int((count / max_val) * bar_area_width) if max_val > 0 else 0
            bar_w = max(bar_w, 4)
            gradient = QLinearGradient(bar_area_left, y, bar_area_left + bar_w, y)
            gradient.setColorAt(0, color)
            lighter = QColor(color)
            lighter.setAlpha(180)
            gradient.setColorAt(1, lighter)
            painter.setBrush(gradient)
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(bar_area_left, y + 2, bar_w, bar_height, 4, 4)
            painter.setPen(QColor(THEME["fg"]))
            painter.setFont(QFont("Consolas", 9, QFont.Bold))
            painter.drawText(bar_area_left + bar_w + 8, y + 17, str(count))
        painter.end()

class NavButton(QPushButton):
    def __init__(self, icon_text, label, parent=None):
        super().__init__(parent)
        self.icon_text = icon_text
        self.label = label
        self.active = False
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(48)
        self.setCheckable(True)
    def set_active(self, active):
        self.active = active
        self.setChecked(active)
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w = self.width()
        h = self.height()
        if self.active:
            painter.fillRect(self.rect(), QColor(THEME["nav_active"]))
            painter.fillRect(0, 4, 3, h - 8, QColor(THEME["nav_active_border"]))
        elif self.underMouse():
            painter.fillRect(self.rect(), QColor(THEME["nav_hover"]))
        painter.setPen(QColor(THEME["accent"] if self.active else THEME["fg2"]))
        painter.setFont(QFont("Segoe UI", 14))
        painter.drawText(QRect(0, 0, 52, h), Qt.AlignCenter, self.icon_text)
        if w > 52:
            painter.setPen(QColor(THEME["fg"] if self.active else THEME["fg2"]))
            painter.setFont(QFont("Segoe UI", 10))
            painter.drawText(QRect(52, 0, w - 56, h), Qt.AlignVCenter | Qt.AlignLeft, self.label)
        painter.end()

class SideNav(QWidget):
    page_changed = pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(180)
        self.buttons = []
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(2)
        items = [("🖥", LANG["nav_console"]), ("📋", LANG["nav_commands"]), ("📊", LANG["nav_stats"]), ("⚙️", LANG["nav_settings"]), ("✏️", LANG["nav_editor"]), ("ℹ️", LANG["nav_about"])]
        for i, (icon, label) in enumerate(items):
            btn = NavButton(icon, label)
            btn.clicked.connect(lambda checked, idx=i: self._on_click(idx))
            layout.addWidget(btn)
            self.buttons.append(btn)
        layout.addStretch()
        self.status_widget = QWidget()
        status_layout = QVBoxLayout(self.status_widget)
        status_layout.setContentsMargins(12, 8, 12, 8)
        self.status_dot = QLabel("● " + LANG["offline"])
        self.status_dot.setStyleSheet(f"color: {THEME['fg2']}; font-size: 10px;")
        status_layout.addWidget(self.status_dot)
        self.cmd_count = QLabel(f"0 {LANG['total_commands']}")
        self.cmd_count.setStyleSheet(f"color: {THEME['fg2']}; font-size: 9px;")
        status_layout.addWidget(self.cmd_count)
        layout.addWidget(self.status_widget)
        self.set_active(0)
    def _on_click(self, idx):
        self.set_active(idx)
        self.page_changed.emit(idx)
    def set_active(self, idx):
        for i, btn in enumerate(self.buttons):
            btn.set_active(i == idx)
    def set_online(self, online):
        if online:
            self.status_dot.setText("● " + LANG["online"])
            self.status_dot.setStyleSheet(f"color: {THEME['success']}; font-size: 10px;")
        else:
            self.status_dot.setText("● " + LANG["offline"])
            self.status_dot.setStyleSheet(f"color: {THEME['fg2']}; font-size: 10px;")
    def set_cmd_count(self, count):
        self.cmd_count.setText(f"{count} {LANG['total_commands']}")
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(THEME["nav_bg"]))
        painter.setPen(QColor(THEME["border"]))
        painter.drawLine(self.width() - 1, 0, self.width() - 1, self.height())
        painter.end()

class CommandsPage(QWidget):
    def __init__(self, commands_dict, parent=None):
        super().__init__(parent)
        self.commands_dict = commands_dict
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        top = QHBoxLayout()
        title = QLabel(f"{LANG['nav_commands']}")
        title.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {THEME['fg']};")
        top.addWidget(title)
        top.addStretch()
        self.reload_btn = QPushButton(LANG["cmd_reload"])
        self.reload_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 8px 16px; border-radius: 6px; font-weight: bold; }}")
        self.reload_btn.setCursor(Qt.PointingHandCursor)
        self.reload_btn.clicked.connect(self.hot_reload)
        top.addWidget(self.reload_btn)
        layout.addLayout(top)
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels([LANG["cmd_name"], LANG["cmd_calls"], LANG["cmd_status"]])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setStyleSheet(f"QTableWidget {{ background-color: {THEME['bg2']}; color: {THEME['fg']}; border: 1px solid {THEME['border']}; border-radius: 6px; }} QTableWidget::item:alternate {{ background-color: {THEME['bg3']}; }} QHeaderView::section {{ background-color: {THEME['bg3']}; color: {THEME['fg']}; padding: 6px; border: none; border-bottom: 1px solid {THEME['border']}; font-weight: bold; }}")
        layout.addWidget(self.table)
        self.refresh_table()
    def refresh_table(self):
        self.table.setRowCount(0)
        cmds = sorted(self.commands_dict.keys())
        self.table.setRowCount(len(cmds))
        for row, cmd in enumerate(cmds):
            name_item = QTableWidgetItem(f".{cmd}")
            name_item.setFont(QFont("Consolas", 10))
            self.table.setItem(row, 0, name_item)
            count = db.get_cmd_count(cmd)
            count_item = QTableWidgetItem(str(count))
            count_item.setTextAlignment(Qt.AlignCenter)
            count_item.setFont(QFont("Consolas", 10, QFont.Bold))
            if count > 0:
                count_item.setForeground(QColor(THEME["accent"]))
            self.table.setItem(row, 1, count_item)
            status_item = QTableWidgetItem(f"{LANG['cmd_active']}")
            status_item.setTextAlignment(Qt.AlignCenter)
            status_item.setForeground(QColor(THEME["success"]))
            self.table.setItem(row, 2, status_item)
    def hot_reload(self):
        add_log("Hot-reload...", "info")
        old_count = len(self.commands_dict)
        for key in list(self.commands_dict.keys()):
            del self.commands_dict[key]
        if not os.path.exists("commands"):
            add_log("commands/ not found", "warning")
            self.refresh_table()
            return
        for file in os.listdir("commands"):
            if file.endswith(".py") and file != "__init__.py":
                cmd_name = file[:-3]
                file_path = os.path.join("commands", file)
                try:
                    spec = importlib.util.spec_from_file_location(cmd_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if hasattr(module, "execute"):
                        self.commands_dict[cmd_name] = module.execute
                        add_log(f"  .{cmd_name}", "success")
                except Exception as e:
                    add_log(f"  {file}: {e}", "error")
        new_count = len(self.commands_dict)
        add_log(f"Hot-reload: {old_count} -> {new_count}", "success")
        self.refresh_table()

class StatsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        top = QHBoxLayout()
        title = QLabel(f"{LANG['nav_stats']}")
        title.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {THEME['fg']};")
        top.addWidget(title)
        top.addStretch()
        refresh_btn = QPushButton("")
        refresh_btn.setFixedSize(36, 36)
        refresh_btn.setStyleSheet(f"QPushButton {{ background: {THEME['bg3']}; color: {THEME['fg']}; border-radius: 6px; font-size: 14px; }}")
        refresh_btn.setCursor(Qt.PointingHandCursor)
        refresh_btn.clicked.connect(self.refresh_chart)
        top.addWidget(refresh_btn)
        layout.addLayout(top)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(f"QScrollArea {{ border: 1px solid {THEME['border']}; border-radius: 6px; }}")
        self.chart = StatsChartWidget()
        scroll.setWidget(self.chart)
        layout.addWidget(scroll)
        self.refresh_chart()
    def refresh_chart(self):
        self.chart.set_data(db.get_all_stats())

class SettingsPage(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        title = QLabel(f"{LANG['nav_settings']}")
        title.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {THEME['fg']};")
        layout.addWidget(title)
        grp_style = f"QGroupBox {{ color: {THEME['fg']}; border: 1px solid {THEME['border']}; border-radius: 8px; margin-top: 10px; padding-top: 10px; }} QGroupBox::title {{ subcontrol-origin: margin; left: 10px; padding: 0 5px; }}"
        edit_style = f"background: {THEME['bg3']}; color: {THEME['fg']}; border: 1px solid {THEME['border']}; border-radius: 6px; padding: 6px;"
        lang_group = QGroupBox(LANG["language"])
        lang_group.setStyleSheet(grp_style)
        lang_layout = QHBoxLayout()
        self.lang_ru = QRadioButton("Russian")
        self.lang_en = QRadioButton("English")
        self.lang_ua = QRadioButton("Ukrainian")
        self.lang_ru.setChecked(settings["language"] == "ru")
        self.lang_en.setChecked(settings["language"] == "en")
        self.lang_ua.setChecked(settings["language"] == "ua")
        lang_layout.addWidget(self.lang_ru)
        lang_layout.addWidget(self.lang_en)
        lang_layout.addWidget(self.lang_ua)
        lang_group.setLayout(lang_layout)
        layout.addWidget(lang_group)
        theme_group = QGroupBox(LANG["theme"])
        theme_group.setStyleSheet(grp_style)
        theme_layout = QHBoxLayout()
        self.theme_combo = QComboBox()
        self.theme_combo.setStyleSheet(f"QComboBox {{ background: {THEME['bg3']}; color: {THEME['fg']}; border: 1px solid {THEME['border']}; border-radius: 6px; padding: 6px; }}")
        for key, data in THEMES.items():
            self.theme_combo.addItem(data["name"], key)
        idx = self.theme_combo.findData(settings["theme"])
        if idx >= 0:
            self.theme_combo.setCurrentIndex(idx)
        theme_layout.addWidget(self.theme_combo)
        theme_group.setLayout(theme_layout)
        layout.addWidget(theme_group)
        api_group = QGroupBox(LANG["telegram_api"])
        api_group.setStyleSheet(grp_style)
        api_layout = QFormLayout()
        api_layout.setSpacing(8)
        api_id, api_hash, phone = load_api()
        self.api_id_edit = QLineEdit()
        self.api_id_edit.setPlaceholderText(LANG["api_id"])
        self.api_id_edit.setStyleSheet(edit_style)
        if api_id:
            self.api_id_edit.setText(str(api_id))
        self.api_hash_edit = QLineEdit()
        self.api_hash_edit.setPlaceholderText(LANG["api_hash"])
        self.api_hash_edit.setStyleSheet(edit_style)
        if api_hash:
            self.api_hash_edit.setText(api_hash)
        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText(LANG["phone_format"])
        self.phone_edit.setStyleSheet(edit_style)
        if phone:
            self.phone_edit.setText(phone)
        for lbl_text, widget in [(LANG["api_id"] + ":", self.api_id_edit), (LANG["api_hash"] + ":", self.api_hash_edit), (LANG["phone"] + ":", self.phone_edit)]:
            lbl = QLabel(lbl_text)
            lbl.setStyleSheet(f"color: {THEME['fg']};")
            api_layout.addRow(lbl, widget)
        api_group.setLayout(api_layout)
        layout.addWidget(api_group)
        self.autostart_cb = QCheckBox(LANG["autostart"])
        self.autostart_cb.setStyleSheet(f"color: {THEME['fg']};")
        self.autostart_cb.setChecked(settings["autostart"])
        layout.addWidget(self.autostart_cb)
        self.tray_cb = QCheckBox(LANG["minimize_to_tray"])
        self.tray_cb.setStyleSheet(f"color: {THEME['fg']};")
        self.tray_cb.setChecked(settings.get("minimize_to_tray", True))
        layout.addWidget(self.tray_cb)
        layout.addStretch()
        save_btn = QPushButton(f"{LANG['save']}")
        save_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 10px 24px; border-radius: 8px; font-weight: bold; font-size: 12px; }}")
        save_btn.setCursor(Qt.PointingHandCursor)
        save_btn.clicked.connect(self.do_save)
        layout.addWidget(save_btn)
    def _get_selected_lang(self):
        if self.lang_ru.isChecked():
            return "ru"
        if self.lang_en.isChecked():
            return "en"
        return "ua"
    def do_save(self):
        global settings, LANG, THEME
        a_id = self.api_id_edit.text().strip()
        a_hash = self.api_hash_edit.text().strip()
        a_phone = self.phone_edit.text().strip()
        if a_id and not a_id.isdigit():
            QMessageBox.warning(self, LANG["error"], LANG["api_id_error"])
            return
        if a_id and a_hash and a_phone:
            save_api(a_id, a_hash, a_phone)
            add_log(f"{LANG['api_saved']}", "success")
        settings["language"] = self._get_selected_lang()
        settings["autostart"] = self.autostart_cb.isChecked()
        settings["theme"] = self.theme_combo.currentData()
        settings["minimize_to_tray"] = self.tray_cb.isChecked()
        save_settings()
        LANG = LANGUAGES[settings["language"]]
        LANG["lang_code"] = settings["language"]
        THEME = THEMES[settings["theme"]]
        add_log(f"{LANG['settings_saved']}", "success")
        reply = QMessageBox.question(self, LANG["restart"], LANG["restart_question"], QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            import subprocess
            subprocess.Popen([sys.executable] + sys.argv)
            QApplication.quit()

class CodeEditorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.current_file = None
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        top_panel = QHBoxLayout()
        self.file_label = QLabel(LANG["select_command"])
        self.file_label.setStyleSheet(f"font-size: 12px; color: {THEME['fg2']};")
        top_panel.addWidget(self.file_label)
        top_panel.addStretch()
        self.save_btn = QPushButton(LANG["save_code"])
        self.save_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 8px 16px; border-radius: 6px; font-weight: bold; }}")
        self.save_btn.clicked.connect(self.save_file)
        top_panel.addWidget(self.save_btn)
        self.delete_btn = QPushButton(LANG["delete"])
        self.delete_btn.setStyleSheet(f"QPushButton {{ background: {THEME['danger']}; color: white; padding: 8px 16px; border-radius: 6px; }}")
        self.delete_btn.clicked.connect(self.delete_command)
        top_panel.addWidget(self.delete_btn)
        self.create_btn = QPushButton(LANG["create_command"])
        self.create_btn.setStyleSheet(f"QPushButton {{ background: {THEME['success']}; color: white; padding: 8px 16px; border-radius: 6px; }}")
        self.create_btn.clicked.connect(self.create_new_command)
        top_panel.addWidget(self.create_btn)
        layout.addLayout(top_panel)
        splitter = QSplitter(Qt.Horizontal)
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.addWidget(QLabel(f"{LANG['nav_commands']}:"))
        self.cmd_list = QListWidget()
        self.cmd_list.itemClicked.connect(self.load_command)
        left_layout.addWidget(self.cmd_list)
        refresh_list_btn = QPushButton(LANG["cmd_reload"])
        refresh_list_btn.clicked.connect(self.refresh_command_list)
        left_layout.addWidget(refresh_list_btn)
        splitter.addWidget(left_widget)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addWidget(QLabel(f"{LANG['code_editor']}:"))
        self.code_editor = QTextEdit()
        self.code_editor.setFont(QFont("Consolas", 10))
        self.code_editor.setStyleSheet(f"QTextEdit {{ background-color: {THEME['bg2']}; color: {THEME['fg']}; border: 1px solid {THEME['border']}; border-radius: 6px; font-family: Consolas; }}")
        right_layout.addWidget(self.code_editor)
        splitter.addWidget(right_widget)
        splitter.setSizes([250, 750])
        layout.addWidget(splitter)
        self.status_label = QLabel("")
        self.status_label.setStyleSheet(f"font-size: 10px; color: {THEME['fg2']}; padding: 5px;")
        layout.addWidget(self.status_label)
        self.refresh_command_list()
    def refresh_command_list(self):
        self.cmd_list.clear()
        commands_dir = "commands"
        if os.path.exists(commands_dir):
            for filename in sorted(os.listdir(commands_dir)):
                if filename.endswith(".py") and not filename.startswith("_"):
                    self.cmd_list.addItem(filename[:-3])
        self.status_label.setText(f"Loaded {self.cmd_list.count()} commands")
    def load_command(self, item):
        cmd_name = item.text()
        filepath = os.path.join("commands", f"{cmd_name}.py")
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    code = f.read()
                self.code_editor.setPlainText(code)
                self.current_file = filepath
                self.file_label.setText(f"Editing: {cmd_name}.py")
                self.status_label.setText(f"Loaded: {cmd_name}")
            except Exception as e:
                self.status_label.setText(f"Error: {e}")
    def save_file(self):
        if not self.current_file:
            self.status_label.setText(LANG["select_command"])
            return
        code = self.code_editor.toPlainText()
        try:
            compile(code, self.current_file, 'exec')
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(code)
            self.status_label.setText(f"Saved: {os.path.basename(self.current_file)}")
            if self.parent and hasattr(self.parent, 'commands'):
                new_commands = load_commands()
                self.parent.commands.update(new_commands)
                if hasattr(self.parent, 'commands_page'):
                    self.parent.commands_page.refresh_table()
        except SyntaxError as e:
            self.status_label.setText(f"Syntax error: {e}")
    def delete_command(self):
        if not self.current_file:
            self.status_label.setText(LANG["select_command"])
            return
        reply = QMessageBox.question(self, LANG["delete"], f"Delete {os.path.basename(self.current_file)}?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.remove(self.current_file)
            self.current_file = None
            self.code_editor.clear()
            self.file_label.setText(LANG["select_command"])
            self.refresh_command_list()
            self.status_label.setText("Command deleted")
    def create_new_command(self):
        dialog = QDialog(self)
        dialog.setWindowTitle(LANG["create_command"])
        dialog.setFixedSize(600, 500)
        dialog.setModal(True)
        dialog.setStyleSheet(make_dialog_style())
        layout = QVBoxLayout(dialog)
        layout.setSpacing(10)
        layout.addWidget(QLabel(LANG["command_name"]))
        name_edit = QLineEdit()
        name_edit.setPlaceholderText("mycommand")
        layout.addWidget(name_edit)
        layout.addWidget(QLabel(LANG["command_code"]))
        code_edit = QTextEdit()
        code_edit.setPlainText('async def execute(event, args, client, db, LANG):\n    if not args:\n        return "Usage: .command <text>"\n    return f"Result: {\\" \\".join(args)}"')
        code_edit.setFont(QFont("Consolas", 10))
        layout.addWidget(code_edit)
        buttons = QHBoxLayout()
        create_btn = QPushButton(LANG["create"])
        create_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 8px 16px; border-radius: 6px; }}")
        cancel_btn = QPushButton(LANG["cancel"])
        buttons.addWidget(create_btn)
        buttons.addWidget(cancel_btn)
        layout.addLayout(buttons)
        def do_create():
            cmd_name = name_edit.text().strip().lower()
            cmd_code = code_edit.toPlainText()
            if not cmd_name:
                QMessageBox.warning(dialog, LANG["error"], "Enter command name")
                return
            if not cmd_name.replace("_", "").isalnum():
                QMessageBox.warning(dialog, LANG["error"], "Invalid name")
                return
            filepath = os.path.join("commands", f"{cmd_name}.py")
            if os.path.exists(filepath):
                reply = QMessageBox.question(dialog, "Exists", f"Overwrite {cmd_name}.py?", QMessageBox.Yes | QMessageBox.No)
                if reply != QMessageBox.Yes:
                    return
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(cmd_code)
            self.refresh_command_list()
            dialog.accept()
            self.status_label.setText(f"Created: {cmd_name}.py")
        create_btn.clicked.connect(do_create)
        cancel_btn.clicked.connect(dialog.reject)
        dialog.exec_()

class AboutPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(16)
        icon_label = QLabel()
        icon_label.setAlignment(Qt.AlignCenter)
        _, pix = load_app_icon(80)
        if pix and not pix.isNull():
            icon_label.setPixmap(pix)
        else:
            icon_label.setText("🍵")
            icon_label.setStyleSheet("font-size: 64px;")
        layout.addWidget(icon_label)
        title = QLabel("T.UserBot Reborn")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {THEME['fg']};")
        layout.addWidget(title)
        version = QLabel(VERSION)
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet(f"font-size: 12px; color: {THEME['fg2']};")
        layout.addWidget(version)
        about = QLabel(LANG["about_text"])
        about.setAlignment(Qt.AlignCenter)
        about.setWordWrap(True)
        about.setStyleSheet(f"font-size: 11px; color: {THEME['fg']};")
        layout.addWidget(about)
        flags = QLabel("RU EN UA")
        flags.setAlignment(Qt.AlignCenter)
        flags.setStyleSheet("font-size: 16px;")
        layout.addWidget(flags)

class ConsolePage(QWidget):
    def __init__(self, commands_dict, parent=None):
        super().__init__(parent)
        self.commands_dict = commands_dict
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        top = QHBoxLayout()
        self.start_btn = QPushButton(LANG["start"])
        self.start_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 10px 24px; border-radius: 8px; font-weight: bold; font-size: 12px; }}")
        self.start_btn.setCursor(Qt.PointingHandCursor)
        top.addWidget(self.start_btn)
        top.addStretch()
        self.cmd_count_label = QLabel(f"{len(self.commands_dict)} {LANG['total_commands']}")
        self.cmd_count_label.setStyleSheet(f"background: {THEME['bg2']}; padding: 6px 12px; border-radius: 16px; color: {THEME['fg']};")
        top.addWidget(self.cmd_count_label)
        layout.addLayout(top)
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setFont(QFont(settings["console_font"], 9))
        self.console.setStyleSheet(f"QTextEdit {{ background-color: {THEME['console_bg']}; color: {THEME['console_fg']}; border: 1px solid {THEME['border']}; border-radius: 6px; padding: 8px; }}")
        layout.addWidget(self.console)
        console_btns = QHBoxLayout()
        clear_btn = QPushButton(LANG["clear"])
        clear_btn.setStyleSheet(f"QPushButton {{ background: {THEME['bg3']}; color: {THEME['fg']}; padding: 6px 14px; border-radius: 6px; }}")
        clear_btn.setCursor(Qt.PointingHandCursor)
        clear_btn.clicked.connect(self.clear_console)
        console_btns.addWidget(clear_btn)
        export_btn = QPushButton(LANG["export"])
        export_btn.setStyleSheet(f"QPushButton {{ background: {THEME['bg3']}; color: {THEME['fg']}; padding: 6px 14px; border-radius: 6px; }}")
        export_btn.setCursor(Qt.PointingHandCursor)
        export_btn.clicked.connect(self.export_logs)
        console_btns.addWidget(export_btn)
        console_btns.addStretch()
        layout.addLayout(console_btns)
    def clear_console(self):
        global log_messages
        log_messages = []
        self.console.clear()
    def export_logs(self):
        path, _ = QFileDialog.getSaveFileName(self, LANG["export_logs"], "", "*.txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                for text, _ in log_messages:
                    f.write(text + "\n")
            add_log(f"{LANG['logs_saved']}", "success")
    def update_console(self):
        lines = log_messages[-settings["console_lines"]:]
        html_parts = []
        for text, msg_type in lines:
            color = self._get_color(msg_type)
            escaped = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            html_parts.append(f'<span style="color:{color};">{escaped}</span>')
        new_html = "<br>".join(html_parts)
        plain_new = "\n".join(t for t, _ in lines)
        if self.console.toPlainText() != plain_new:
            self.console.setHtml(f'<pre style="font-family:{settings["console_font"]};font-size:9pt;margin:0;padding:0;">{new_html}</pre>')
            sb = self.console.verticalScrollBar()
            sb.setValue(sb.maximum())
    def _get_color(self, msg_type):
        mapping = {"success": THEME["success"], "error": THEME["error_color"], "warning": THEME["warning"], "info": THEME["info"], "cmd": THEME["accent"], "default": THEME["console_fg"]}
        return mapping.get(msg_type, THEME["console_fg"])

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #0D1117;")
        self.setFixedSize(450, 500)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)
        self.icon_label = QLabel()
        self.icon_label.setAlignment(Qt.AlignCenter)
        _, pixmap = load_app_icon(80)
        if pixmap and not pixmap.isNull():
            self.icon_label.setPixmap(pixmap)
        else:
            self.icon_label.setText("🍵")
            self.icon_label.setStyleSheet("font-size: 72px; color: #4CAF50;")
        layout.addWidget(self.icon_label)
        title = QLabel("T.UserBot Reborn")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        layout.addWidget(title)
        version_lbl = QLabel(VERSION)
        version_lbl.setAlignment(Qt.AlignCenter)
        version_lbl.setStyleSheet("font-size: 12px; color: #8B949E;")
        layout.addWidget(version_lbl)
        layout.addSpacing(20)
        self.status_label = QLabel(LANG["loading"])
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 11px; color: #C9D1D9;")
        layout.addWidget(self.status_label)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(3)
        self.progress.setStyleSheet("QProgressBar { border: none; background-color: #21262D; } QProgressBar::chunk { background-color: #238636; }")
        layout.addWidget(self.progress)
        self.center_on_screen()
    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)
    def update_progress(self, value, status):
        self.progress.setValue(value)
        self.status_label.setText(status)
        QApplication.processEvents()

class FirstRunDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T.UserBot Reborn")
        self.setFixedSize(520, 540)
        self.setModal(True)
        self.setup_ui()
        self.center_on_screen()
    def setup_ui(self):
        self.setStyleSheet("QDialog { background-color: #0D1117; } QLabel { color: #C9D1D9; } QLineEdit { background-color: #161B22; border: 1px solid #30363D; border-radius: 6px; padding: 8px; color: #C9D1D9; } QLineEdit:focus { border: 1px solid #238636; } QRadioButton { color: #C9D1D9; spacing: 8px; } QGroupBox { color: #C9D1D9; border: 1px solid #30363D; border-radius: 8px; margin-top: 10px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; } QPushButton { background-color: #238636; border: none; border-radius: 6px; padding: 10px; color: white; font-weight: bold; } QPushButton:hover { background-color: #2EA043; } QPushButton#cancel { background-color: #21262D; } QPushButton#cancel:hover { background-color: #30363D; }")
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        title = QLabel("T.UserBot Reborn")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        layout.addWidget(title)
        subtitle = QLabel(LANG["first_run_subtitle"])
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 12px; color: #8B949E;")
        layout.addWidget(subtitle)
        lang_group = QGroupBox(LANG["lang_group"])
        lang_layout = QHBoxLayout()
        self.ru_btn = QRadioButton("Russian")
        self.en_btn = QRadioButton("English")
        self.ua_btn = QRadioButton("Ukrainian")
        self.ru_btn.setChecked(True)
        lang_layout.addWidget(self.ru_btn)
        lang_layout.addWidget(self.en_btn)
        lang_layout.addWidget(self.ua_btn)
        lang_group.setLayout(lang_layout)
        layout.addWidget(lang_group)
        api_group = QGroupBox(LANG["telegram_api"])
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        self.api_id_edit = QLineEdit()
        self.api_id_edit.setPlaceholderText(LANG["api_id"])
        form_layout.addRow(LANG["api_id"] + ":", self.api_id_edit)
        self.api_hash_edit = QLineEdit()
        self.api_hash_edit.setPlaceholderText(LANG["api_hash"])
        form_layout.addRow(LANG["api_hash"] + ":", self.api_hash_edit)
        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText(LANG["phone_format"])
        form_layout.addRow(LANG["phone"] + ":", self.phone_edit)
        api_group.setLayout(form_layout)
        layout.addWidget(api_group)
        btn_layout = QHBoxLayout()
        save_btn = QPushButton(LANG["first_run_save"])
        save_btn.clicked.connect(self.save_and_continue)
        cancel_btn = QPushButton(LANG["first_run_exit"])
        cancel_btn.setObjectName("cancel")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)
    def _get_lang(self):
        if self.ru_btn.isChecked():
            return "ru"
        if self.en_btn.isChecked():
            return "en"
        return "ua"
    def save_and_continue(self):
        lang = self._get_lang()
        L = LANGUAGES[lang]
        api_id = self.api_id_edit.text().strip()
        api_hash = self.api_hash_edit.text().strip()
        phone = self.phone_edit.text().strip()
        if not api_id or not api_id.isdigit():
            QMessageBox.warning(self, L["error"], L["api_id_error"])
            return
        if not api_hash:
            QMessageBox.warning(self, L["error"], L["api_hash_error"])
            return
        if not phone:
            QMessageBox.warning(self, L["error"], L["phone_error"])
            return
        save_api(api_id, api_hash, phone)
        settings["language"] = lang
        settings["theme"] = "dark"
        save_settings()
        self.accept()

class MainWindow(QMainWindow):
    show_code_signal = pyqtSignal(str)
    show_password_signal = pyqtSignal()
    def __init__(self, commands):
        super().__init__()
        self.commands = commands
        self.bot_running = False
        self.code_result = None
        self.password_result = None
        self.code_event = None
        self.password_event = None
        self._drag_pos = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(1000, 700)
        self.resize(1100, 800)
        icon, _ = load_app_icon()
        self.setWindowIcon(icon)
        self.setup_tray()
        self.setup_ui()
        self.apply_theme()
        self.center_on_screen()
        self.show_code_signal.connect(self.show_code_dialog)
        self.show_password_signal.connect(self.show_password_dialog)
        add_log(f"{LANG['app_title']} | {TEAM}", "info")
        add_log(f"{len(commands)} {LANG['total_commands']}", "info")
        if settings["autostart"]:
            QTimer.singleShot(1000, self.toggle_bot)
    def setup_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        icon, _ = load_app_icon()
        self.tray_icon.setIcon(icon)
        self.tray_icon.setToolTip("T.UserBot Reborn")
        tray_menu = QMenu()
        show_action = tray_menu.addAction(LANG["tray_show"])
        show_action.triggered.connect(self.tray_show_window)
        tray_menu.addSeparator()
        start_action = tray_menu.addAction(LANG["start"])
        start_action.triggered.connect(self.toggle_bot)
        self.tray_start_action = start_action
        tray_menu.addSeparator()
        quit_action = tray_menu.addAction(LANG["tray_quit"])
        quit_action.triggered.connect(self.quit_app)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.show()
    def tray_show_window(self):
        self.showNormal()
        self.activateWindow()
        self.raise_()
    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.tray_show_window()
    def tray_notify(self, title, message):
        if self.tray_icon.isVisible():
            self.tray_icon.showMessage(title, message, QSystemTrayIcon.Information, 3000)
    def closeEvent(self, event):
        if settings.get("minimize_to_tray", True) and self.tray_icon.isVisible():
            event.ignore()
            self.hide()
            self.tray_notify("T.UserBot Reborn", LANG["tray_minimized"])
        else:
            self.quit_app()
    def quit_app(self):
        global bot_running
        if bot_running and bot_client:
            try:
                asyncio.run_coroutine_threadsafe(bot_client.disconnect(), self._bot_loop)
            except:
                pass
        self.tray_icon.hide()
        QApplication.quit()
    def setup_ui(self):
        central = QWidget()
        central.setObjectName("central")
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        title_bar = QWidget()
        title_bar.setObjectName("title_bar")
        title_bar.setFixedHeight(50)
        title_bar.mousePressEvent = self.mouse_press
        title_bar.mouseMoveEvent = self.mouse_move
        title_bar.mouseReleaseEvent = self.mouse_release
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(15, 0, 12, 0)
        icon_label = QLabel()
        _, pix = load_app_icon(24)
        if pix and not pix.isNull():
            icon_label.setPixmap(pix)
        else:
            icon_label.setText("🍵")
        title_layout.addWidget(icon_label)
        title_label = QLabel("T.UserBot Reborn")
        title_label.setStyleSheet("font-size: 13px; font-weight: bold;")
        title_layout.addWidget(title_label)
        version_label = QLabel(VERSION)
        version_label.setStyleSheet("font-size: 10px; color: gray;")
        title_layout.addWidget(version_label)
        flag_map = {"ru": "RU", "en": "EN", "ua": "UA"}
        lang_flag = QLabel(flag_map.get(settings["language"], ""))
        lang_flag.setStyleSheet("font-size: 11px; font-weight: bold; color: gray;")
        title_layout.addWidget(lang_flag)
        title_layout.addStretch()
        self.status_dot = QLabel("●")
        self.status_dot.setStyleSheet("font-size: 12px; color: gray;")
        title_layout.addWidget(self.status_dot)
        self.status_text = QLabel(LANG["offline"])
        self.status_text.setStyleSheet("font-size: 10px; color: gray;")
        title_layout.addWidget(self.status_text)
        btn_style = "QPushButton { background: transparent; border: none; font-size: 14px; padding: 6px; border-radius: 4px; } QPushButton:hover { background: rgba(128,128,128,0.2); }"
        min_btn = QPushButton("─")
        min_btn.setCursor(Qt.PointingHandCursor)
        min_btn.setStyleSheet(btn_style)
        min_btn.clicked.connect(self.showMinimized)
        title_layout.addWidget(min_btn)
        self.max_btn = QPushButton("□")
        self.max_btn.setCursor(Qt.PointingHandCursor)
        self.max_btn.setStyleSheet(btn_style)
        self.max_btn.clicked.connect(self.toggle_maximize)
        title_layout.addWidget(self.max_btn)
        close_btn = QPushButton("✕")
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet(btn_style + " QPushButton:hover { background: #DA3633; color: white; }")
        close_btn.clicked.connect(self.close)
        title_layout.addWidget(close_btn)
        main_layout.addWidget(title_bar)
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setObjectName("separator")
        sep.setFixedHeight(1)
        main_layout.addWidget(sep)
        body = QWidget()
        body.setObjectName("body")
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)
        self.side_nav = SideNav()
        self.side_nav.page_changed.connect(self.switch_page)
        self.side_nav.set_cmd_count(len(self.commands))
        body_layout.addWidget(self.side_nav)
        self.page_stack = QStackedWidget()
        self.page_stack.setObjectName("page_stack")
        self.console_page = ConsolePage(self.commands)
        self.console_page.start_btn.clicked.connect(self.toggle_bot)
        self.page_stack.addWidget(self.console_page)
        self.commands_page = CommandsPage(self.commands)
        self.page_stack.addWidget(self.commands_page)
        self.stats_page = StatsPage()
        self.page_stack.addWidget(self.stats_page)
        self.settings_page = SettingsPage(self)
        self.page_stack.addWidget(self.settings_page)
        self.code_editor_page = CodeEditorPage(self)
        self.page_stack.addWidget(self.code_editor_page)
        self.about_page = AboutPage()
        self.page_stack.addWidget(self.about_page)
        body_layout.addWidget(self.page_stack)
        main_layout.addWidget(body)
        self.timer = QTimer()
        self.timer.timeout.connect(self._timer_tick)
        self.timer.start(300)
    def _timer_tick(self):
        self.console_page.update_console()
        self.side_nav.set_cmd_count(len(self.commands))
        self.console_page.cmd_count_label.setText(f"{len(self.commands)} {LANG['total_commands']}")
    def switch_page(self, idx):
        self.page_stack.setCurrentIndex(idx)
        if idx == 2:
            self.stats_page.refresh_chart()
        if idx == 1:
            self.commands_page.refresh_table()
        if idx == 4:
            self.code_editor_page.refresh_command_list()
    def apply_theme(self):
        self.setStyleSheet(f"#central, #body, #page_stack {{ background-color: {THEME['bg']}; }} #title_bar {{ background-color: {THEME['title_bg']}; }} #separator {{ background-color: {THEME['border']}; }} QWidget {{ color: {THEME['fg']}; }} QStackedWidget {{ background-color: {THEME['bg']}; }}")
    def mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
    def mouse_move(self, event):
        if self._drag_pos is not None and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
    def mouse_release(self, event):
        self._drag_pos = None
    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.max_btn.setText("□")
        else:
            self.showMaximized()
            self.max_btn.setText("❐")
    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)
    def show_code_dialog(self, phone):
        dialog = QDialog(self)
        dialog.setWindowTitle(LANG["auth_title"])
        dialog.setModal(True)
        dialog.setFixedSize(400, 300)
        dialog.setStyleSheet(make_dialog_style())
        layout = QVBoxLayout(dialog)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)
        icon = QLabel("")
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet("font-size: 48px;")
        layout.addWidget(icon)
        title = QLabel(LANG["auth_code"])
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(title)
        info = QLabel(f"{LANG['auth_code_sent']}\n{phone}")
        info.setAlignment(Qt.AlignCenter)
        info.setWordWrap(True)
        layout.addWidget(info)
        code_edit = QLineEdit()
        code_edit.setPlaceholderText("00000")
        code_edit.setAlignment(Qt.AlignCenter)
        code_edit.setStyleSheet("font-size: 18px; padding: 8px;")
        layout.addWidget(code_edit)
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton(LANG["auth_submit"])
        ok_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 8px 16px; border-radius: 6px; font-weight: bold; }}")
        cancel_btn = QPushButton(LANG["cancel"])
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
        result = {"code": None, "ok": False}
        def on_ok():
            result["code"] = code_edit.text().strip()
            result["ok"] = True
            dialog.accept()
        def on_cancel():
            result["ok"] = False
            dialog.reject()
        ok_btn.clicked.connect(on_ok)
        cancel_btn.clicked.connect(on_cancel)
        code_edit.returnPressed.connect(on_ok)
        dialog.exec_()
        self.code_result = result["code"] if result["ok"] and result["code"] else None
        if self.code_event:
            self.code_event.set()
    def show_password_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle(LANG["auth_2fa_title"])
        dialog.setModal(True)
        dialog.setFixedSize(400, 300)
        dialog.setStyleSheet(make_dialog_style())
        layout = QVBoxLayout(dialog)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)
        icon = QLabel("")
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet("font-size: 48px;")
        layout.addWidget(icon)
        title = QLabel(LANG["auth_2fa_title"])
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(title)
        info = QLabel(LANG["auth_2fa_info"])
        info.setAlignment(Qt.AlignCenter)
        info.setWordWrap(True)
        layout.addWidget(info)
        pass_edit = QLineEdit()
        pass_edit.setEchoMode(QLineEdit.Password)
        pass_edit.setStyleSheet("font-size: 14px; padding: 8px;")
        layout.addWidget(pass_edit)
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton(LANG["auth_submit"])
        ok_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 8px 16px; border-radius: 6px; font-weight: bold; }}")
        cancel_btn = QPushButton(LANG["cancel"])
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
        result = {"password": None, "ok": False}
        def on_ok():
            result["password"] = pass_edit.text().strip()
            result["ok"] = True
            dialog.accept()
        def on_cancel():
            result["ok"] = False
            dialog.reject()
        ok_btn.clicked.connect(on_ok)
        cancel_btn.clicked.connect(on_cancel)
        pass_edit.returnPressed.connect(on_ok)
        dialog.exec_()
        self.password_result = result["password"] if result["ok"] and result["password"] else None
        if self.password_event:
            self.password_event.set()
    def toggle_bot(self):
        if not load_api()[0]:
            QMessageBox.warning(self, LANG["api_settings"], LANG["no_api"])
            return
        if not self.bot_running:
            self.bot_running = True
            self.console_page.start_btn.setText(LANG["stop"])
            self.console_page.start_btn.setStyleSheet(f"QPushButton {{ background: {THEME['danger']}; color: white; padding: 10px 24px; border-radius: 8px; font-weight: bold; font-size: 12px; }}")
            self.status_dot.setStyleSheet(f"font-size: 12px; color: {THEME['success']};")
            self.status_text.setText(LANG["online"])
            self.status_text.setStyleSheet(f"font-size: 10px; color: {THEME['success']};")
            self.side_nav.set_online(True)
            self.tray_start_action.setText(LANG["stop"])
            add_log(LANG["bot_started"], "success")
            self.tray_notify("T.UserBot Reborn", LANG["tray_bot_started"])
            self.bot_thread = threading.Thread(target=self.run_bot_thread, args=(self.commands,), daemon=True)
            self.bot_thread.start()
        else:
            self.bot_running = False
            self._update_ui_stopped()
            add_log(LANG["bot_stopped"], "warning")
            self.tray_notify("T.UserBot Reborn", LANG["tray_bot_stopped"])
            if bot_client:
                asyncio.run_coroutine_threadsafe(bot_client.disconnect(), self._bot_loop)
    def _update_ui_stopped(self):
        self.bot_running = False
        self.console_page.start_btn.setText(LANG["start"])
        self.console_page.start_btn.setStyleSheet(f"QPushButton {{ background: {THEME['accent']}; color: white; padding: 10px 24px; border-radius: 8px; font-weight: bold; font-size: 12px; }}")
        self.status_dot.setStyleSheet("font-size: 12px; color: gray;")
        self.status_text.setText(LANG["offline"])
        self.status_text.setStyleSheet("font-size: 10px; color: gray;")
        self.side_nav.set_online(False)
        self.tray_start_action.setText(LANG["start"])
    def run_bot_thread(self, commands):
        self._bot_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._bot_loop)
        self._bot_loop.run_until_complete(self.run_bot_async(commands))
    async def run_bot_async(self, commands):
        global bot_client, bot_running
        api_id, api_hash, phone = load_api()
        if not api_id:
            add_log(LANG["no_api"], "error")
            return
        client = TelegramClient("data/userbot", int(api_id), api_hash)
        try:
            add_log(LANG["auth_connecting"], "info")
            await client.connect()
            if not await client.is_user_authorized():
                add_log(LANG["auth_waiting"], "info")
                await client.send_code_request(phone)
                self.code_result = None
                self.code_event = threading.Event()
                self.show_code_signal.emit(phone)
                self.code_event.wait()
                if not self.code_result:
                    add_log(LANG["cancel"], "error")
                    await client.disconnect()
                    self._update_ui_stopped()
                    return
                try:
                    await client.sign_in(phone, self.code_result)
                    add_log(LANG["auth_success"], "success")
                except SessionPasswordNeededError:
                    add_log("2FA required", "warning")
                    self.password_result = None
                    self.password_event = threading.Event()
                    self.show_password_signal.emit()
                    self.password_event.wait()
                    if not self.password_result:
                        add_log(LANG["cancel"], "error")
                        await client.disconnect()
                        self._update_ui_stopped()
                        return
                    try:
                        await client.sign_in(password=self.password_result)
                        add_log(LANG["auth_success"], "success")
                    except Exception as e:
                        add_log(f"{e}", "error")
                        await client.disconnect()
                        self._update_ui_stopped()
                        return
            bot_client = client
            bot_running = True
            me = await client.get_me()
            add_log(f"{LANG['bot_started']}: {me.first_name}", "success")
            add_log(f"{len(commands)} {LANG['commands_loaded']}", "info")
            @client.on(events.NewMessage(outgoing=True))
            async def handler(event):
                if not event.text or not event.text.startswith(settings["command_prefix"]):
                    return
                parts = event.text[len(settings["command_prefix"]):].split()
                if not parts:
                    return
                cmd = parts[0].lower()
                args = parts[1:]
                db.stat(cmd)
                add_log(f"CMD: {settings['command_prefix']}{cmd}", "cmd")
                if cmd in commands:
                    try:
                        current_lang = LANG.copy()
                        current_lang["lang_code"] = settings["language"]
                        result = await commands[cmd](event, args, client, db, current_lang)
                        if result:
                            await event.edit(str(result))
                    except Exception as e:
                        add_log(f".{cmd}: {e}", "error")
                        await event.edit(f"Error: {e}")
                else:
                    add_log(f"{LANG['unknown_cmd']}: {cmd}", "warning")
            await client.run_until_disconnected()
        except Exception as e:
            add_log(f"{e}", "error")
        finally:
            bot_running = False
            self._update_ui_stopped()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setQuitOnLastWindowClosed(False)
    icon, _ = load_app_icon()
    app.setWindowIcon(icon)
    if not os.path.exists("data/api_data.json"):
        splash = SplashScreen()
        splash.show()
        for i in range(0, 101, 20):
            splash.update_progress(i, f"{i}%")
            time.sleep(0.05)
        splash.close()
        first = FirstRunDialog()
        if first.exec_() != QDialog.Accepted:
            sys.exit(0)
    splash = SplashScreen()
    splash.show()
    for i in range(0, 101, 10):
        splash.update_progress(i, f"{LANG['loading']} {i}%")
        time.sleep(0.05)
    splash.update_progress(100, LANG["done"])
    time.sleep(0.3)
    splash.close()
    window = MainWindow(load_commands())
    window.show()
    sys.exit(app.exec_())
