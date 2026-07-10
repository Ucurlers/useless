# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: SupportQueue
def weekly_stats(data):
    from collections import defaultdict, Counter
    weeks = defaultdict(lambda: {'total': 0, 'resolved': 0, 'by_priority': Counter(), 'by_status': Counter()})
    for item in data:
        d = item['date'].weekday()
        week_key = (d + 1) * 7 - 6
        weeks[week_key]['total'] += 1
        if item.get('resolved'):
            weeks[week_key]['resolved'] += 1
        p = item.get('priority', 'normal')
        weeks[week_key]['by_priority'][p] += 1
        s = item.get('status', 'open')
        weeks[week_key]['by_status'][s] += 1
    return {k: dict(v) for k, v in sorted(weeks.items())}
