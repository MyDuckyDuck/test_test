# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: DeskQueue
def check_overdue_reminders():
    """Проверка просроченных напоминаний: находит задачи, чей срок истёк, но они ещё в статусе 'pending'."""
    overdue = []
    for task in desk_queue.get_tasks():
        if (task.status == "pending" and
                task.due_date is not None and
                datetime.now() > task.due_date):
            task.status = "overdue"
            overdue.append(task)
    return overdue
