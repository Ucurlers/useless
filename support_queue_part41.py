# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: SupportQueue
def dry_run(self, op, record):
    """Execute operation in dry-run mode, logging instead of modifying state."""
    if not self._dry_run:
        return self.execute(op, record)
    log = self._dry_run_log
    if op == "create":
        log.append(f"[DRY-RUN] Created ticket #{record['id']}")
    elif op == "update":
        log.append(f"[DRY-RUN] Updated ticket #{record['id']}")
    elif op == "delete":
        log.append(f"[DRY-RUN] Deleted ticket #{record['id']}")
    elif op == "assign":
        log.append(f"[DRY-RUN] Assigned ticket #{record['id']} to {record['assignee']}")
    elif op == "reply":
        log.append(f"[DRY-RUN] Added reply to ticket #{record['id']}")
    else:
        log.append(f"[DRY-RUN] Executed {op} on ticket #{record.get('id', 'unknown')}")
    return log
