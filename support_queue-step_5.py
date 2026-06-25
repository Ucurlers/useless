# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: SupportQueue
def delete_ticket(ticket_id: int) -> bool:
    if not data.get("tickets"):
        return False
    tickets = data["tickets"]
    for i, ticket in enumerate(tickets):
        if ticket["id"] == ticket_id:
            del tickets[i]
            break
    else:
        raise ValueError(f"Ticket with id {ticket_id} not found")

def delete_agent(agent_id: int) -> bool:
    if not data.get("agents"):
        return False
    agents = data["agents"]
    for i, agent in enumerate(agents):
        if agent["id"] == agent_id:
            del agents[i]
            break
    else:
        raise ValueError(f"Agent with id {agent_id} not found")

def delete_history_entry(history_id: int) -> bool:
    if not data.get("history"):
        return False
    history = data["history"]
    for i, entry in enumerate(history):
        if entry["id"] == history_id:
            del history[i]
            break
    else:
        raise ValueError(f"History entry with id {history_id} not found")
