# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: SupportQueue
def export_state_to_json(queue_data):
    import json
    def serialize(obj):
        if isinstance(obj, set):
            return list(sorted(obj))
        if hasattr(obj, '__dict__'):
            d = {}
            for k in obj.__dict__:
                v = getattr(obj, k)
                d[k] = serialize(v)
            return d
        raise TypeError(f"Unsupported type: {type(obj)}")
    def format_response(r):
        if r is None:
            return {"id": None}
        res = {"id": r.id}
        if hasattr(r, 'status'):
            res['status'] = serialize(r.status)
        else:
            res['status'] = "pending"
        return res
    def format_ticket(t):
        t_data = {
            "id": t.ticket_id,
            "subject": t.subject,
            "priority": int(t.priority),
            "assigned_to": serialize(t.assigned_to) if hasattr(t, 'assigned_to') else None,
            "status": serialize(t.status) if hasattr(t, 'status') else "new",
            "responses": [format_response(r) for r in t.responses] if hasattr(t, 'responses') and t.responses else []
        }
        return t_data
    def format_agent(a):
        a_data = {
            "id": a.agent_id,
            "name": serialize(a.name),
            "current_ticket": serialize(a.current_ticket) if hasattr(a, 'current_ticket') else None
        }
        return a_data
    tickets_list = [format_ticket(t) for t in queue_data.tickets]
    agents_list = [format_agent(a) for a in queue_data.agents]
    output = {
        "tickets": tickets_list,
        "agents": agents_list,
        "timestamp": str(queue_data.timestamp) if hasattr(queue_data, 'timestamp') else None
    }
    return json.dumps(output, ensure_ascii=False, indent=2)
