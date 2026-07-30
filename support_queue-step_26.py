# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: SupportQueue
def demo():
    from support_queue import SupportQueue, Ticket, Priority, Status, Role, Agent, Customer, Channel

    q = SupportQueue()

    for i in range(10):
        ticket = Ticket(
            id=f"T{i+1:03d}",
            title="Demo ticket " + str(i+1),
            priority=Priority.HIGH if i % 2 == 0 else Priority.LOW,
            status=Status.OPEN,
            channel=Channel.EMAIL,
            description=f"Sample issue {i+1} for demo purposes.",
        )
        q.add(ticket)

    agent = Agent(name="Alice", role=Role.SUPPORT, email="alice@demo.com")
    customer = Customer(name="Bob", email="bob@demo.com")

    ticket0 = q.get(0)
    reply = f"Hi Bob! We are looking into your {ticket0.title}. Please wait."
    agent.respond(ticket0, reply)

    ticket1 = q.get(1)
    customer.respond(ticket1, "Thanks for the quick response.")

    ticket2 = q.get(2)
    agent.transfer(ticket2, customer)

    print("Demo queue created with 10 tickets.")
    print(f"Top priority: {q.top()}")
    print(f"Queue size: {len(q)}")
