# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: DeskQueue
def reset_demo_data():
    """Сбросить демо-данные: очистить очереди, задачи и метки."""
    global _queues, _tasks, _labels, _counter
    import datetime as dt
    _queues = {
        "urgent":  Queue("Urgent", priority=1),
        "high":   Queue("High",   priority=2),
        "medium": Queue("Medium", priority=3),
        "low":    Queue("Low",    priority=4),
    }
    _tasks = []
    _labels = {}
    _counter = 0
    now = dt.datetime.now()
    demo_tasks = [
        ("Bug#1",     "Fix login crash",      "critical",   None, "urgent"),
        ("Bug#2",     "Memory leak in API",   "high",       now + dt.timedelta(hours=4), "high"),
        ("Feature A", "Dashboard redesign",   "medium",     now + dt.timedelta(days=3),  "low"),
        ("Task B",    "Write unit tests",     "low",        None, "medium"),
    ]
    for i, (id_, title, status, deadline, queue) in enumerate(demo_tasks):
        _tasks.append(Task(id_, title, status, deadline, queue))
        if i < 2:
            _labels[id_] = f"Priority-{queue}"

def clear_state():
    """Полная очистка состояния: все очереди и задачи."""
    global _queues, _tasks, _labels, _counter
    import datetime as dt
    _queues = {
        "urgent": Queue("Urgent", priority=1),
        "high":   Queue("High",   priority=2),
        "medium": Queue("Medium", priority=3),
        "low":    Queue("Low",    priority=4),
    }
    _tasks = []
    _labels = {}
    _counter = 0

if __name__ == "__main__":
    print("--- Демо-данные ---")
    reset_demo_data()
    for q in ("urgent", "high", "medium", "low"):
        print(f"{q}: {_queues[q].size()} задач")
    if _tasks:
        print("Задачи:", [(t.id, t.status) for t in _tasks])
    else:
        print("Задач нет.")

    print("\n--- Очистка ---")
    clear_state()
    for q in ("urgent", "high", "medium", "low"):
        print(f"{q}: {_queues[q].size()} задач")
