# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: SupportQueue
def check_integrity_and_repair():
    """Проверяет целостность очереди и репарирует простые проблемы."""
    if not queue:
        print("Очередь пуста.")
        return
    integrity_errors = []
    for i, ticket in enumerate(queue):
        if not isinstance(ticket, dict):
            integrity_errors.append(f"Биллет {i} не является словарем.")
            continue
        if "id" not in ticket:
            integrity_errors.append(f"Биллет {i} не имеет ID.")
        if "user" not in ticket:
            integrity_errors.append(f"Биллет {i} не имеет пользователя.")
        if "priority" not in ticket:
            ticket["priority"] = "normal"
            integrity_errors.append(f"Биллет {i} не имеет приоритета, установлен по умолчанию.")
        if "status" not in ticket:
            ticket["status"] = "new"
            integrity_errors.append(f"Биллет {i} не имеет статуса, установлен по умолчанию.")
        if "answers" not in ticket:
            ticket["answers"] = []
            integrity_errors.append(f"Биллет {i} не имеет истории ответов, инициализирована.")
        if "priority" not in ("urgent", "high", "normal", "low"):
            ticket["priority"] = "normal"
            integrity_errors.append(f"Биллет {i} имеет некорректный приоритет, установлен по умолчанию.")
    if integrity_errors:
        print("Обнаружены и исправлены проблемы целостности:")
        for err in integrity_errors:
            print(f"  - {err}")
    else:
        print("Целостность данных подтверждена.")

check_integrity_and_repair()
