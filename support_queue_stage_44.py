# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: SupportQueue
def backup_data_file():
    import shutil, datetime
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"support_queue_backup_{timestamp}.json")
    shutil.copy2(DATA_FILE, backup_path)
    print(f"Backup saved to {backup_path}")
