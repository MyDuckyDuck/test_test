# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: DeskQueue
def remove_task(task_id: int) -> bool:
    """Удалить задачу по ID, вернуть True если удалили, False если запись отсутствовала."""
    if task_id not in tasks_db:
        print(f"Задача с ID {task_id} не найдена.")
        return False
    
    del tasks_db[task_id]
    print(f"Задача с ID {task_id} успешно удалена.")
    return True

def remove_task_by_status(status_filter: str) -> int:
    """Удалить все задачи со статусом status_filter, вернуть количество удаленных."""
    removed_count = 0
    for task_id in list(tasks_db.keys()):
        if tasks_db[task_id].status == status_filter:
            del tasks_db[task_id]
            print(f"Задача {task_id} (статус: {status_filter}) удалена.")
            removed_count += 1
    return removed_count
