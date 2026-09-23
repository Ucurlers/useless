# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: SupportQueue
def _format_ticket_status(ticket):
    """Возвращает читаемый статус обращения."""
    if ticket.status == "open":
        return "ОТКРЫТА"
    elif ticket.status == "in_progress":
        return "В ОБРАБОТКЕ"
    elif ticket.status == "resolved":
        return "РЕШЕНА"
    elif ticket.status == "closed":
        return "ЗАКРЫТА"
    elif ticket.status == "escalated":
        return "УСЛУГОВАНА"
    return "НЕИЗВЕСТЕН"

def _format_agent_display(agent):
    """Возвращает отображаемое имя агента."""
    return f"{agent.name} ({agent.role})"

def _format_priority_label(priority):
    """Возвращает ярлык приоритета."""
    labels = {
        "low": "Низкий",
        "medium": "Средний",
        "high": "Высокий",
        "critical": "Критический"
    }
    return labels.get(priority, "Неизвестный")

def _format_ticket_summary(ticket):
    """Формирует краткое описание обращения."""
    return (
        f"ID: {ticket.id} | "
        f"Тема: {ticket.subject} | "
        f"Пользователь: {ticket.author_name} | "
        f"Приоритет: {_format_priority_label(ticket.priority)} | "
        f"Статус: {_format_ticket_status(ticket)} | "
        f"Агент: {_format_agent_display(ticket.agent)} | "
        f"Ответов: {ticket.answer_count}"
    )

def _format_agent_summary(agent):
    """Формирует краткое описание агента."""
    return (
        f"Имя: {agent.name} | "
        f"Роль: {agent.role} | "
        f"Текущие задачи: {agent.active_tickets} | "
        f"Обработано всего: {agent.total_resolved}"
    )

# Пример использования:
# print(_format_ticket_summary(ticket))
# print(_format_agent_summary(agent))
