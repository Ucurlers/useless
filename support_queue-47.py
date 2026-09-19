# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: SupportQueue
def demo():
    queue = SupportQueue()
    queue.add_ticket("Клиент A", "Проблема с логин", "Критический", "Техподдержка")
    queue.add_ticket("Клиент B", "Забыл пароль", "Средний", "Техподдержка")
    queue.add_ticket("Клиент C", "Оформить возврат", "Низкий", "Менеджер")
    
    print("=== Очередь поддержки ===")
    for ticket in queue.list_tickets():
        print(f"  [{ticket.priority}] {ticket.id}: {ticket.subject} (от: {ticket.customer})")
    
    print("\n--- Обработка очереди ---")
    while queue.has_tickets():
        ticket = queue.next_ticket()
        if ticket is None:
            break
        print(f"  Обрабатываем: {ticket.subject}")
        queue.respond(ticket, "Решено! Спасибо за обращение.")
    
    print("\n=== История ответов ===")
    for resp in queue.history:
        print(f"  {resp}")
