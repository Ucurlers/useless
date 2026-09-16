# === Stage 45: Добавь восстановление из резервной копии ===
# Project: SupportQueue
import json, os
from datetime import datetime

BACKUP_FILE = 'support_backup.json'

def load_backup():
    if not os.path.exists(BACKUP_FILE):
        print(f"Резервная копия не найдена: {BACKUP_FILE}")
        return None
    try:
        with open(BACKUP_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Резервное копирование успешно загружено ({len(data.get('tickets', []))} тикетов)")
        return data
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка загрузки резервной копии: {e}")
        return None
