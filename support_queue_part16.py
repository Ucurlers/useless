# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: SupportQueue
def monthly_stats(self):
    """Return a dict mapping month (YYYY-MM) to total tickets."""
    stats = {}
    for ticket in self._tickets:
        if ticket["status"] != "open":
            continue
        date_str = ticket["created_at"].strftime("%Y-%m")
        stats[date_str] = stats.get(date_str, 0) + 1
    return stats
