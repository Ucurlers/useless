# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: SupportQueue
def archive_records(queue, days_threshold=30):
    """Archive records older than `days_threshold` days (or completed)."""
    import datetime
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=days_threshold)
    archived_ids = set()
    for i in range(len(queue)):
        item = queue[i]
        if isinstance(item, dict):
            status = item.get("status", "").lower()
            created = item.get("created_at")
            is_old = False
            try:
                if isinstance(created, str):
                    created_date = datetime.date.fromisoformat(created)
                else:
                    created_date = created.date() if hasattr(created, "date") else None
                if created_date and created_date < cutoff:
                    is_old = True
            except Exception:
                pass
            if status in ("resolved", "closed"):
                is_old = True
        elif isinstance(item, list) and item:
            status = item[0].get("status", "").lower() if isinstance(item[0], dict) else ""
            created = item[0].get("created_at") if len(item) > 0 else None
            is_old = False
            try:
                if isinstance(created, str):
                    created_date = datetime.date.fromisoformat(created)
                else:
                    created_date = getattr(created, "date", lambda: None)()
                if created_date and created_date < cutoff:
                    is_old = True
            except Exception:
                pass
            if status in ("resolved", "closed"):
                is_old = True
        elif isinstance(item, dict):
            status = item.get("status", "").lower()
            created = item.get("created_at")
            is_old = False
            try:
                if isinstance(created, str):
                    created_date = datetime.date.fromisoformat(created)
                else:
                    created_date = getattr(created, "date", lambda: None)()
                if created_date and created_date < cutoff:
                    is_old = True
            except Exception:
                pass
        else:
            continue
        if is_old:
            archived_ids.add(id(item))
    return list(archived_ids)
