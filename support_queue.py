# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: SupportQueue
from typing import List, Optional, Dict
import uuid
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Ticket:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    subject: str = ""
    priority: int = 1
    status: str = "open"
    created_at: datetime = field(default_factory=datetime.now)
    history: List[Dict] = field(default_factory=list)

@dataclass
class Agent:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    current_ticket_id: Optional[str] = None

def get_demo_data() -> tuple[List[Ticket], List[Agent]]:
    tickets = [
        Ticket(subject="Ошибка входа", priority=3),
        Ticket(subject="Вопрос по тарифу", priority=1),
        Ticket(subject="Критический баг", priority=5),
        Ticket(subject="Запрос на возврат", priority=2),
    ]
    agents = [
        Agent(name="Алексей"),
        Agent(name="Мария"),
        Agent(name="Дмитрий"),
    ]
    return tickets, agents

if __name__ == "__main__":
    demo_tickets, demo_agents = get_demo_data()
    print(f"Инициализация очереди: {len(demo_tickets)} заявок и {len(demo_agents)} операторов.")
