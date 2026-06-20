# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SupportQueue
class Ticket:
    def __init__(self, id, subject, description, priority='normal'):
        self.id = int(id) if isinstance(id, str) else id
        self.subject = str(subject).strip()
        self.description = str(description).strip()
        self.priority = priority.lower() in ('low', 'medium', 'high') and priority or 'normal'

class Agent:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя исполнителя должно быть непустой строкой")
        self.name = name.strip()

# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SupportQueue
class Ticket:
    def __init__(self, id_, subject, priority='medium', description='', status='open'):
        if not isinstance(id_, int) or id_ <= 0: raise ValueError("ID must be a positive integer")
        if not isinstance(subject, str) or len(subject.strip()) < 3: raise ValueError("Subject too short")
        valid_priorities = {'low', 'medium', 'high'}
        if priority not in valid_priorities: raise ValueError(f"Priority must be one of {valid_priorities}")
        self.id = id_
        self.subject = subject.strip()
        self.priority = priority
        self.description = description
        self.status = status

class Agent:
    def __init__(self, name, email):
        if not isinstance(name, str) or len(name.strip()) < 2: raise ValueError("Name too short")
        if '@' not in email or '.' not in email.split('@')[-1]: raise ValueError("Invalid email format")
        self.name = name.strip()
        self.email = email

class SupportQueueSystem:
    def __init__(self):
        self.tickets = {}
        self.agents = {}
    
    def add_ticket(self, ticket_data):
        if not isinstance(ticket_data, dict) or 'id' not in ticket_data: return None
        try:
            t = Ticket(
                id_=ticket_data['id'],
                subject=ticket_data.get('subject', ''),
                priority=ticket_data.get('priority', 'medium'),
                description=ticket_data.get('description', ''),
                status=ticket_data.get('status', 'open')
            )
        except ValueError: return None
        if t.id in self.tickets: return None
        self.tickets[t.id] = t
        return t
    
    def add_agent(self, agent_data):
        if not isinstance(agent_data, dict) or 'name' not in agent_data: return None
        try:
            a = Agent(
                name=agent_data['name'],
                email=agent_data.get('email', '')
            )
        except ValueError: return None
        if a.name in self.agents: return None
        self.agents[a.name] = a
        return a
