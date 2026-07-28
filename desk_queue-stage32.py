# === Stage 32: Добавь журнал действий пользователя ===
# Project: DeskQueue
from datetime import datetime, timedelta

class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, user_id, action_type, description, task_id=None):
        entry = {
            'timestamp': datetime.now(),
            'user_id': user_id,
            'action_type': action_type,
            'description': description,
            'task_id': task_id,
        }
        self._entries.append(entry)

    def get_log(self):
        return list(reversed(sorted(self._entries, key=lambda e: e['timestamp'])))

    def clear(self):
        self._entries.clear()


def get_action_logger():
    return ActionLog()
