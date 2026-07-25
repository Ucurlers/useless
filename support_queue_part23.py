# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: SupportQueue
def print_queue_table(queue):
    """Compact console table for SupportQueue."""
    if not queue:
        print("  Queue is empty.")
        return
    headers = ["ID", "Subject", "Priority", "Status", "Executor"]
    widths = [len(h) for h in headers]
    rows = []
    for idx, item in enumerate(queue, start=1):
        row = [str(item.id), item.subject[:25], str(item.priority), item.status, str(item.executor)]
        rows.append([w.strip() if isinstance(w, str) else w for w in row])
        widths = [max(widths[i], max(len(r[i]) for r in rows)) for i in range(len(headers))]
    print("  " + " | ".join(f"{h:<{widths[i]}}" for i, h in enumerate(headers)))
    print("  " + "-+-".join("-" * widths[i] for i in range(len(headers))))
    for row in rows:
        print("  " + " | ".join(f"{str(cell):<{widths[i]}}" for i, cell in enumerate(row)))
