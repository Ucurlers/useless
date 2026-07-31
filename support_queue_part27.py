# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: SupportQueue
def reset_demo_data():
    """Сбросить все демо-данные в очередь: клиентов, техподдержку, обращения и ответы."""
    demo_customers = [
        {"id": "C001", "name": "Алексей Иванов", "email": "alex@example.com"},
        {"id": "C002", "name": "Мария Петрова", "email": "maria@example.com"},
        {"id": "C003", "name": "Дмитрий Сидоров", "email": "dmitry@example.com"},
    ]
    demo_support = [
        {"id": "S001", "name": "Техподдержка 1", "role": "support_agent"},
        {"id": "S002", "name": "Техподдержка 2", "role": "support_agent"},
        {"id": "S003", "name": "Администратор", "role": "admin"},
    ]
    demo_tickets = [
        {"ticket_id": "T001", "customer_id": "C001", "subject": "Проблема с доступом", "priority": 1, "status": "open", "assigned_to": None},
        {"ticket_id": "T002", "customer_id": "C002", "subject": "Вопрос по тарифу", "priority": 3, "status": "in_progress", "assigned_to": "S001"},
        {"ticket_id": "T003", "customer_id": "C003", "subject": "Ошибка при оплате", "priority": 2, "status": "open", "assigned_to": None},
    ]
    demo_responses = [
        {"ticket_id": "T001", "from_user": "S002", "response_text": "Спасибо за обращение. Мы проверим вашу проблему.", "created_at": "2024-03-01"},
        {"ticket_id": "T002", "from_user": "S001", "response_text": "Пожалуйста, уточните ваш тарифный план.", "created_at": "2024-03-02"},
    ]

    global customers, support_staff, tickets, responses
    customers = demo_customers
    support_staff = demo_support
    tickets = demo_tickets
    responses = demo_responses
    print("Демо-данные успешно сброшены.")


def clear_state():
    """Полностью очистить все данные и сбросить глобальное состояние."""
    global customers, support_staff, tickets, responses
    customers = []
    support_staff = []
    tickets = []
    responses = []
    print("Состояние полностью очищено.")


if __name__ == "__main__":
    reset_demo_data()
    clear_state()
