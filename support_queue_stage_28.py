# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: SupportQueue
def print_metrics(queue: "SupportQueue") -> None:
    """Расчёт и вывод ключевых метрик очереди."""
    total = len(queue)
    if not total:
        return
    avg_priority = sum(p for _, p, _ in queue) / total
    priority_counts = {}
    for _, p, _ in queue:
        priority_counts[p] = priority_counts.get(p, 0) + 1

    print("=" * 45)
    print("SupportQueue — Ключевые метрики")
    print(f"{'='*45}")
    print(f"Всего обращений: {total}")
    print(f"Средний приоритет: {avg_priority:.2f}")
    for p in sorted(priority_counts):
        print(f"  Приоритет {p}: {priority_counts[p]}")

    if total > 1:
        unique_responders = len({resp[0] for resp in queue})
        print(f"Уникальных исполнителей: {unique_responders}")
