# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: SupportQueue
class SupportQueueFilter:
    def __init__(self, queue):
        self.queue = queue
    
    def filter_by_status(self, statuses=None):
        if not statuses:
            return list(self.queue)
        return [t for t in self.queue if t.status in statuses]
    
    def filter_by_category(self, category=None):
        if not category:
            return list(self.queue)
        return [t for t in self.queue if t.category == category]
    
    def filter_by_tags(self, tags=None):
        if not tags:
            return list(self.queue)
        return [t for t in self.queue if any(tag in t.tags for tag in tags)]
    
    def filter_combined(self, statuses=None, category=None, tags=None):
        results = self.filter_by_status(statuses)
        if category:
            results = [r for r in results if r.category == category]
        if tags:
            results = [r for r in results if any(tag in r.tags for tag in tags)]
        return results
