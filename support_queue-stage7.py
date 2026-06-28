# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: SupportQueue
def sort_tickets(tickets, key='date'):
    if not tickets: return []
    reverse = {'priority': True, 'name': False}.get(key, False)
    date_key = lambda t: (t['created_at'] or 0, -1 * t.get('priority', 0)) if key == 'date' else None
    name_key = lambda t: t.get('subject', '').lower() if key == 'name' else None
    priority_key = lambda t: (-1 * t.get('priority', 0), -(t['created_at'] or 0)) if key == 'priority' else None
    sort_keys = {
        'date': date_key,
        'priority': priority_key,
        'name': name_key
    }
    return sorted(tickets, key=sort_keys.get(key, lambda x: (x['created_at'] or 0, -1 * x.get('priority', 0), x.get('subject', ''))), reverse=reverse)
