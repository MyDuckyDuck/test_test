# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: DeskQueue
class DeskQueue:
    def __init__(self):
        self._tasks = []
    
    def add_task(self, title: str, deadline: float, status: int = 0, tags: list[str] | None = None) -> dict:
        task_id = len(self._tasks) + 1
        entry = {
            "id": task_id,
            "title": title,
            "deadline": deadline,
            "status": status,
            "tags": tags or [],
            "created_at": time.time()
        }
        self._tasks.append(entry)
        return entry

import time
