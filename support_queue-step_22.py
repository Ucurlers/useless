# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: SupportQueue
def check_overdue_reminders(queue):
    """Проверяет просроченные напоминания для обращений поддержки."""
    now = datetime.now()
    overdue = []
    for ticket in queue:
        if not hasattr(ticket, 'last_reminder') or not hasattr(ticket, 'created_at'):
            continue
        days_since_last = (now - ticket.last_reminder).days
        if days_since_last >= 30 and days_since_last < 60:
            overdue.append((ticket, days_since_last))
    return overdue

if __name__ == "__main__":
    print("Тестовый запуск SupportQueue")
