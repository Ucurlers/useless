# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: SupportQueue
class Template:
    """Шаблон для быстрого создания записей очереди."""
    def __init__(self, name, subject, description='', priority=1, assignee=None, category='general'):
        self.name = name
        self.subject = subject
        self.description = description
        self.priority = priority
        self.assignee = assignee
        self.category = category
        self.id = None

    def to_record(self, queue):
        record = Record(
            id=self.id,
            queue=queue,
            subject=self.subject,
            description=self.description,
            priority=self.priority,
            assignee=self.assignee,
            category=self.category,
            created_at=now(),
            status='new'
        )
        return record
