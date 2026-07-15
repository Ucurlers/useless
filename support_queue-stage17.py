# === Stage 17: Добавь группировку записей по категориям ===
# Project: SupportQueue
from collections import defaultdict


class CategoryGroup:
    def __init__(self):
        self._groups = defaultdict(list)

    def add(self, record):
        category = getattr(record, "category", "general")
        self._groups[category].append(record)
        return True

    @property
    def groups(self):
        return dict(self._groups)


def group_support_records(records, key_field="category"):
    grouped = defaultdict(list)
    for r in records:
        k = getattr(r, key_field, "general")
        grouped[k].append(r)
    return dict(grouped)
