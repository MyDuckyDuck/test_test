# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: DeskQueue
def demo():
    print("=== DeskQueue Demo ===")
    q = Queue()
    task1 = Task("fix_login", priority="high", deadline=3600, status="open", tags=["bug"], created_at=time.time())
    task2 = Task("write_docs", priority="low", deadline=7200, status="pending", tags=["docs"], created_at=time.time())
    q.add(task1)
    q.add(task2)
    print(f"Queue size: {q.size}")
    for t in sorted(q.get_all(), key=lambda x: x.priority):
        print(f"- [{t.status}] {t.name} (priority={t.priority}, deadline={t.deadline}s)")
