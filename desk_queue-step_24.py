# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: DeskQueue
def print_task_summary(task: Task) -> None:
    if task is None:
        print("  [нет данных]")
        return
    print(f"  ID={task.id} | статус={task.status.value}")
    print(f"     задача='{task.task_name}' | срок={task.deadline.strftime('%d.%m')}")
    tags = ", ".join(t.name for t in task.tags) if task.tags else "-"
    print(f"     теги={tags}")
