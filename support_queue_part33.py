# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: SupportQueue
class UndoableStack:
    """Stack of UndoableEntry that supports undoing the last action."""
    
    def __init__(self):
        self._stack = []
    
    def push(self, entry: UndoableEntry) -> None:
        self._stack.append(entry)
    
    def undo(self) -> Optional[UndoableEntry]:
        if not self._stack:
            return None
        return self._stack.pop()
    
    @property
    def size(self) -> int:
        return len(self._stack)
    
    def __len__(self) -> int:
        return len(self._stack)
    
    def __iter__(self):
        return iter(self._stack)
