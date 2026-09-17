# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: SupportQueue
def migrate_to_v46():
    """Миграция v45 → v46: добавляем поле `history` в структуру обращения.

    В версии v45 структура обращения выглядела так:
      {
        "id": str,
        "priority": int,
        "assignee": str | None,
        "created_at": str,
        "status": str,
        "response": str | None
      }

    В версии v46 добавляем поле `history` — список словечек с ответами,
    чтобы можно было отслеживать историю переписки в одном объекте.
    """
    OLD_SCHEMA = {
        "id": str,
        "priority": int,
        "assignee": str | None,
        "created_at": str,
        "status": str,
        "response": str | None,
    }
    NEW_SCHEMA = OLD_SCHEMA | {
        "history": list[str],
    }

    # Переводим существующие обращения из v45 в v46
    migrated = []
    for ticket in support_queue:
        new_ticket = {
            "id": ticket["id"],
            "priority": ticket["priority"],
            "assignee": ticket["assignee"],
            "created_at": ticket["created_at"],
            "status": ticket["status"],
            "response": ticket["response"],
            "history": [],
        }
        migrated.append(new_ticket)

    support_queue.clear()
    support_queue.extend(migrated)
    return migrated
