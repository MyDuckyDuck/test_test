# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: DeskQueue
import time
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

@dataclass
class Task:
    id: int
    title: str
    description: str
    deadline: datetime
    priority: int  # 1-5, 1 is highest
    status: TaskStatus = TaskStatus.PENDING
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

class DeskQueue:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str, deadline: datetime, priority: int = 3, tags: Optional[List[str]] = None) -> Task:
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            deadline=deadline,
            priority=priority,
            status=TaskStatus.PENDING,
            tags=tags or []
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_pending_tasks(self) -> List[Task]:
        return [t for t in self.tasks if t.status == TaskStatus.PENDING]

    def get_overdue_tasks(self) -> List[Task]:
        now = datetime.now()
        return [t for t in self.tasks if t.status != TaskStatus.COMPLETED and t.deadline < now]

def demo():
    queue = DeskQueue()
    
    # Пример данных: задачи с разными приоритетами и сроками
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)
    
    queue.add_task("Сделать отчет", "Подготовить квартальный отчет", next_week, priority=2, tags=["отчет", "финансы"])
    queue.add_task("Позвонить клиенту", "Обсудить детали проекта", tomorrow, priority=1, tags=["клиент"])
    queue.add_task("Купить продукты", "Молоко, хлеб, яйца", today + timedelta(hours=2), priority=3, tags=["личное"])
    
    print(f"Добавлено задач: {len(queue.tasks)}")
    print(f"Ожидание задач: {len(queue.get_pending_tasks())}")
    print(f"Передержанные задачи: {len(queue.get_overdue_tasks())}")

if __name__ == "__main__":
    demo()
