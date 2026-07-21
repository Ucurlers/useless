# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: SupportQueue
class Reminder:
    def __init__(self, message, due_date):
        self.message = message
        self.due_date = due_date
    
    @property
    def is_overdue(self):
        return datetime.now() > self.due_date
    
    def to_dict(self):
        return {"message": self.message, "due_date": self.due_date.isoformat()}
    
    @classmethod
    def from_dict(cls, data):
        return cls(message=data["message"], due_date=datetime.fromisoformat(data["due_date"]))


class ReminderQueue:
    def __init__(self):
        self._reminders = []
    
    def add(self, reminder):
        self._reminders.append(reminder)
        return len(self._reminders) - 1
    
    def get_overdue(self):
        return [r for r in self._reminders if r.is_overdue]
    
    def clear_overdue(self):
        overdue = self.get_overdue()
        for reminder in overdue:
            self._reminders.remove(reminder)
        return len(overdue)


def add_reminder_system(queue_data, reminders_data):
    queue_obj = SupportQueue(**queue_data)
    reminders_queue = ReminderQueue()
    
    reminder_objs = [Reminder.from_dict(r) for r in reminders_data]
    for i, r in enumerate(reminder_objs):
        reminders_queue.add(r)
    
    overdue = reminders_queue.get_overdue()
    if overdue:
        queue_obj.log("SYSTEM", "⚠️ Напоминания о пересроченных задачах:")
        for rem in overdue:
            queue_obj.log("SYSTEM", f"  - {rem.message}")
    
    return queue_obj, reminders_queue


def get_reminder_status(reminder):
    if reminder.is_overdue:
        return "⚠️ Пересрочен"
    elif datetime.now() > reminder.due_date - timedelta(days=1):
        return "🔴 Скоро срок"
    else:
        return "✅ В норме"


def print_reminder_summary(reminders_queue):
    overdue = reminders_queue.get_overdue()
    if not overdue:
        print("Напоминания: все в порядке")
        return
    
    print(f"⚠️ {len(overdue)} пересроченных напоминаний:")
    for rem in overdue:
        print(f"  - {rem.message}")


def save_reminders(reminders_queue, filepath):
    with open(filepath, "w") as f:
        import json
        data = [r.to_dict() for r in reminders_queue._reminders]
        json.dump(data, f, indent=2)
