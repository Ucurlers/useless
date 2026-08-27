# === Stage 32: Добавь журнал действий пользователя ===
# Project: SupportQueue
class UserActionLog:
    def __init__(self):
        self._log = []

    def log(self, user, action, detail=""):
        self._log.append({"user": user, "action": action, "detail": detail, "timestamp": time.time()})

    def get_log(self):
        return self._log
