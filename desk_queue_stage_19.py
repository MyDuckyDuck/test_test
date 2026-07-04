# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: DeskQueue
def archive_completed_tasks(tasks, days_threshold=30):
    from datetime import datetime, timedelta
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    archived_count = 0
    for task in tasks:
        if task['status'] == 'completed' or (task.get('created_at') and datetime.fromisoformat(task['created_at']) < cutoff_date):
            task['archived'] = True
            archived_count += 1
    return archived_count
