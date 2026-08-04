# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: SupportQueue
class Config:
    def __init__(self, settings):
        self._settings = settings
    
    def get(self, key, default=None):
        return self._settings.get(key, default)
    
    @property
    def max_queue_size(self):
        return self.get("max_queue_size", 100)

class SupportQueue:
    def __init__(self, name="SupportQueue", config=None):
        self.name = name
        self.config = Config({}) if config is None else Config(config)
    
    def add_ticket(self, title, description, priority=3, executor_id=None, **metadata):
        ticket = Ticket(title=title, description=description, 
                        priority=priority, executor_id=executor_id, 
                        metadata=metadata)
        self._tickets.append(ticket)
        return ticket
    
    def get_next_ticket(self):
        if not self._tickets:
            print("Queue is empty!")
            return None
        
        tickets = sorted(self._tickets, key=lambda t: t.priority)
        next_ticket = tickets[0]
        
        if len(tickets) > 1 and next_ticket.executor_id is not None:
            other_tickets = [t for t in tickets if t != next_ticket]
            print(f"Priority queue has {len(other_tickets)} more high-priority tickets...")
        
        return next_ticket
    
    def get_history(self, ticket):
        history = []
        for record in self._history:
            if record.ticket_id == ticket.id:
                history.append(record)
        return sorted(history, key=lambda h: h.timestamp)
    
    @property
    def tickets_info(self):
        info_list = []
        for i, ticket in enumerate(self._tickets, 1):
            info_list.append({
                "id": ticket.id,
                "title": ticket.title,
                "priority": ticket.priority,
                "executor_id": ticket.executor_id,
            })
        return info_list

    def __del__(self):
        print(f"SupportQueue '{self.name}' is being deleted.")
