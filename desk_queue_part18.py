# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: DeskQueue
class TaskTagManager:
    def __init__(self, task):
        self.task = task
        self.tags = set(task.get('tags', [])) if isinstance(task, dict) else set()

    def add_tag(self, tag_name):
        if not tag_name.strip():
            return False
        self.tags.add(tag_name.lower().strip())
        self._update_task_data()
        return True

    def remove_tag(self, tag_name):
        tag_to_remove = tag_name.lower().strip()
        if tag_to_remove in self.tags:
            self.tags.discard(tag_to_remove)
            self._update_task_data()
            return True
        return False

    def has_tag(self, tag_name):
        return tag_name.lower().strip() in self.tags

    def list_tags(self):
        return sorted(list(self.tags))

    def _update_task_data(self):
        if isinstance(self.task, dict) and 'tags' not in self.task:
            self.task['tags'] = []
        if isinstance(self.task, dict):
            self.task['tags'] = list(self.tags)
