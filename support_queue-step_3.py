# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: SupportQueue
class SupportQueue:
    def __init__(self):
        self.records = []
    
    def add_ticket(self, ticket_id, priority, requester, description):
        record = {
            "id": ticket_id,
            "priority": priority,
            "requester": requester,
            "description": description,
            "status": "open",
            "assigned_to": None,
            "created_at": datetime.now().isoformat(),
            "history": []
        }
        self.records.append(record)
        return record
    
    def assign_ticket(self, ticket_id, agent_name):
        for record in self.records:
            if record["id"] == ticket_id and record["status"] == "open":
                record["assigned_to"] = agent_name
                record["history"].append(f"Assigned to {agent_name}")
                return True
        return False
    
    def get_ticket(self, ticket_id):
        for record in self.records:
            if record["id"] == ticket_id:
                return record
        return None

from datetime import datetime
