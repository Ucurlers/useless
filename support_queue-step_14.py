# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: SupportQueue
def generate_summary(agents, queue):
    """Генерация краткой сводки по текущим данным очереди."""
    lines = []
    
    # Статистика агентов
    active = sum(1 for a in agents.values() if a["status"] == "active")
    busy = sum(1 for a in agents.values() if a["status"] == "busy")
    total = len(agents)
    lines.append(f"Агенты: {active} активны, {busy} занято (всего {total})")
    
    # Статистика очереди
    high_priority = sum(1 for q in queue.values() if q.get("priority", 0) >= 3)
    low_priority = sum(1 for q in queue.values() if q.get("priority", 0) <= 2)
    total_queue = len(queue)
    
    lines.append(f"Очередь: {high_priority} высокий приоритет, "
                 f"{low_priority} низкий (всего {total_queue})")
    
    # Время ожидания для активных агентов
    if agents and queue:
        avg_wait = sum(q.get("wait_time", 0) for q in queue.values()) / total_queue
        lines.append(f"Ср. время ожидания: {avg_wait:.1f} сек")
    
    return "\n".join(lines)
