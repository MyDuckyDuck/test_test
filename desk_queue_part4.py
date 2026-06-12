# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: DeskQueue
def edit_task(task_id, updates):
    """Редактирует задачу по ID, возвращая обновлённую запись или None."""
    if task_id not in tasks:
        return None
    
    for key, value in updates.items():
        if hasattr(tasks[task_id], key) and value is not None:
            setattr(tasks[task_id], key, value)
    
    print(f"Задача #{task_id} обновлена.")
    return tasks[task_id]
