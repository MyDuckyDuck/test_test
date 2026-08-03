# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: DeskQueue
class DataIntegrityChecker:
    def __init__(self, db):
        self.db = db

    def check_integrity(self):
        errors = []
        for task in self.db.tasks.values():
            if not isinstance(task.status, str) or len(task.status) == 0:
                errors.append(f"Task {task.id}: invalid status '{task.status}'")
            if task.deadline and (not isinstance(task.deadline, datetime) or task.deadline < datetime(1970, 1, 1)):
                errors.append(f"Task {task.id}: invalid deadline")
        for queue in self.db.queues.values():
            if not isinstance(queue.name, str):
                errors.append(f"Queue: missing name")
        return errors

    def repair_simple(self):
        tasks = list(self.db.tasks.values())
        repaired = []
        for task in tasks:
            if not task.status or task.status == '':
                task.status = 'pending'
                repaired.append(task.id)
            elif task.status not in ('pending', 'active', 'completed', 'cancelled'):
                task.status = 'pending'
                repaired.append(task.id)
        return repaired
