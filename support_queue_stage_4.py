# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: SupportQueue
def edit_ticket(ticket_id: int, updates: dict) -> Optional[dict]:
    if ticket_id not in tickets:
        raise ValueError(f"Ticket {ticket_id} not found")
    
    original = tickets[ticket_id].copy()
    for key, value in updates.items():
        if key in ['id', 'status']:
            continue  # Запрещаем изменение ID и статуса при редактировании
        setattr(tickets[ticket_id], key, value)
    
    history_entry = {
        "action": "edit",
        "ticket_id": ticket_id,
        "timestamp": datetime.now().isoformat(),
        "changes": {k: {"old": original.get(k), "new": v} for k, v in updates.items() if k != 'id'}
    }
    
    tickets[ticket_id].history.append(history_entry)
    return tickets[ticket_id]
