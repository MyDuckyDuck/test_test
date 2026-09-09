# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: DeskQueue
def _compact_task_repr(task: dict) -> str:
    """Return a one-line readable summary of a task dict."""
    parts = [
        f"id={task.get('id')}",
        f"queue={task.get('queue')}",
        f"status={task.get('status')}",
        f"deadline={task.get('deadline')}",
        f"tags={task.get('tags')}",
        f"priority={task.get('priority')}",
    ]
    return " | ".join(parts)

def _compact_queue_summary(queue_name: str, tasks: list) -> str:
    """Return a one-line summary of a queue's current state."""
    statuses = {}
    for t in tasks:
        s = t.get("status", "unknown")
        statuses[s] = statuses.get(s, 0) + 1
    total = len(tasks)
    sorted_statuses = sorted(statuses.items(), key=lambda x: -x[1])
    return f"{queue_name}: {total} tasks | " + " | ".join(f"{s}={c}" for s, c in sorted_statuses)
