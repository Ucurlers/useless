# === Stage 20: Добавь восстановление записей из архива ===
# Project: SupportQueue
def restore_from_archive(archive_path: str, queue: "SupportQueue") -> int:
    """Восстанавливает записи из архива в очередь."""
    if not os.path.exists(archive_path):
        raise FileNotFoundError(f"Архив не найден: {archive_path}")
    
    count = 0
    with open(archive_path, 'r') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) == 5:
                record = {
                    'id': parts[0],
                    'subject': parts[1],
                    'priority': int(parts[2]),
                    'assignee_id': parts[3] if parts[3].isdigit() else None,
                    'status': parts[4],
                    'answers': [],
                }
                queue.add(record)
                count += 1
    
    return count

def save_to_archive(queue: "SupportQueue", archive_path: str) -> int:
    """Сохраняет записи из очереди в архив."""
    if not os.path.exists(os.path.dirname(archive_path)):
        os.makedirs(os.path.dirname(archive_path))
    
    with open(archive_path, 'w') as f:
        for record in queue.records:
            line = '|'.join([
                str(record['id']),
                record['subject'],
                str(record['priority']),
                str(record['assignee_id']) if record['assignee_id'] else '',
                record['status'],
            ]) + '\n'
            f.write(line)
    
    return len(queue.records)
