# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: SupportQueue
def suggest_next_action(state: dict) -> str:
    """На основе текущего состояния очереди возвращает рекомендацию следующего действия."""
    queue = state.get("queue", [])
    if not queue:
        return "Очередь пуста. Добавьте новый тикет."

    high = [t for t in queue if t.get("priority", 0) >= 3]
    if high:
        return f"Обратите внимание на приоритетные тикеты: {'; '.join(t['id'] for t in high)}"

    pending = [t for t in queue if t["status"] == "pending" and not t.get("assigned_to")]
    if pending:
        return "Назначьте исполнителей на тикеты со статусом pending."

    in_progress = [t for t in queue if t["status"] == "in_progress" and not t.get("responses")]
    if in_progress:
        return "Проверьте прогресс по тикетам без ответов."

    overdue = [t for t in queue if t["status"] in ("pending", "in_progress") and t.get("created_at") and (now - t["created_at"]) > 7200]
    if overdue:
        return "Некоторые тикеты ждут слишком долго. Рассмотрите их статус."

    return "Все тикеты обработаны. Можете обновить статусы или добавить новые обращения."
