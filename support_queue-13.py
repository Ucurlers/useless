# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: SupportQueue
def search_support_tickets(self, query: str) -> list[SupportTicket]:
    if not query.strip():
        return []
    q = query.lower()
    results = []
    for t in self._tickets:
        fields = [str(t.ticket_id), t.subject, t.description, (t.status or '').lower(), t.priority]
        if any(q in f for f in fields):
            results.append(t)
    return sorted(results, key=lambda x: ({'critical': 0, 'high': 1, 'medium': 2}[x.priority.lower()], x.created_at), reverse=True)[:25]
