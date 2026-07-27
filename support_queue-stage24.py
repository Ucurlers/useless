# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: SupportQueue
from datetime import datetime, timedelta

def print_ticket(ticket):
    if not ticket:
        return "Очередь пуста."
    name = ticket.get("name", "Без имени")
    priority = ticket.get("priority", 3)
    status = ticket.get("status", "Новая")
    history = ticket.get("history", [])
    if not history:
        return f"Тикет #{ticket['id']} | {name} | Приоритет {priority} ({'Критичный' if priority == 1 else 'Высокий' if priority == 2 else 'Низкий'}) | Статус: {status}"
    last = history[-1]
    date = datetime.fromisoformat(last["timestamp"]) if "timestamp" in last else None
    time_str = date.strftime("%d.%m %H:%M") if date else "?"
    return f"Тикет #{ticket['id']} | {name} | Приоритет {priority} ({'Критичный' if priority == 1 else 'Высокий' if priority == 2 else 'Низкий'}) | Статус: {status} | Последнее сообщение от {last.get('from', '?')}: \"{last['text']}\" [{time_str}]"
