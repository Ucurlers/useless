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
