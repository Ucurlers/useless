# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: SupportQueue
def add_tags(self, tags):
    if not isinstance(tags, (str, list)):
        raise TypeError("tags must be str or list of str")
    tag_set = set(t.strip().lower() for t in tags)
    for t in tag_set:
        if t and t not in self._tags:
            self._tags.add(t)

def remove_tags(self, tags):
    if not isinstance(tags, (str, list)):
        raise TypeError("tags must be str or list of str")
    for t in tags:
        stripped = t.strip().lower()
        if stripped and stripped in self._tags:
            self._tags.discard(stripped)

@property
def tag_list(self):
    return sorted(self._tags)
