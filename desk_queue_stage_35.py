# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: DeskQueue
import time


def get_next_action(state: dict) -> str:
    """Генерирует рекомендацию следующего действия на основе текущего состояния системы."""
    now = int(time.time())
    task = state.get("current_task", {})
    queue = state.get("queue", [])

    if not task and not queue:
        return "Система пуста. Добавьте новую задачу через DeskTask().enqueue(task_id, description).start() или загрузите данные из JSON-файла."

    deadline = task.get("deadline") or 0
    status = task.get("status", "pending")

    if deadline > 0 and (now - deadline) >= 120:
        return f"⚠️ Задача '{task.get('description', 'Неизвестная')}' подошла к дедлайну! Осталось {max(0, int((deadline - now) / 60))} минут. Используйте DeskTask().reassign(task_id, new_assignee) или DeskTask().extend_deadline(task_id, hours)."

    if not queue and status != "active":
        return "Текущая задача завершена или не активна. Запустите следующую из очереди: DeskTask().start_next() или DeskTask().enqueue(task_id, description).start()."

    if task.get("priority") == "high" and status != "completed":
        return f"🔥 Высокий приоритет! Задача '{task.get('description', 'Неизвестная')}' требует немедленного внимания. Используйте DeskTask().complete(task_id) после выполнения."

    return f"✅ Текущая задача в статусе '{status}'. Продолжайте работу или выполните DeskTask().complete(task_id) для завершения."
