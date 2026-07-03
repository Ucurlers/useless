# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: SupportQueue
import json, os, uuid, time
DATA_FILE = "support_queue.json"
def save_state():
    data = {
        "tickets": [t for t in globals().get("TICKETS", [])],
        "agents": list(globals().get("AGENTS", {}).keys()),
        "history": list(globals().get("RESPONSES", {}).items())
    }
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка сохранения данных: {e}")

def load_state():
    if not os.path.exists(DATA_FILE):
        return None
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        globals()["TICKETS"] = data.get("tickets", [])
        globals()["AGENTS"] = {aid: {"name": aid} for aid in data.get("agents", [])}
        globals()["RESPONSES"] = dict(data.get("history", []))
        return True
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        return False

def init_persistence():
    if load_state() is None and not os.path.exists(DATA_FILE):
        save_state()
