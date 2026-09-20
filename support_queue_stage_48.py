# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: SupportQueue
class SupportQueue:
    def __init__(self):
        self._queue = []
        self._respondents = []
        self._history = []

    def add_request(self, text, priority="normal", respondent=None):
        request = {
            "text": text,
            "priority": priority,
            "respondent": respondent,
            "status": "new"
        }
        self._queue.append(request)
        self._queue.sort(key=lambda x: {"urgent": 0, "normal": 1, "low": 2}.get(x["priority"], 1))
        return request

    def get_next(self):
        if not self._queue:
            return None
        next_req = self._queue.pop(0)
        if next_req["status"] == "new":
            next_req["status"] = "processing"
            if next_req["respondent"] not in self._respondents:
                self._respondents.append(next_req["respondent"])
        return next_req

    def respond(self, request_id, response_text):
        for req in self._queue:
            if req["text"] == request_id:
                req["status"] = "answered"
                req["response"] = response_text
                self._history.append({
                    "request": req,
                    "response": response_text,
                    "timestamp": self._get_timestamp()
                })
                return True
        return False

    def get_history(self):
        return self._history

    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().isoformat()
