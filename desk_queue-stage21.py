# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: DeskQueue
class Reminder:
    def __init__(self, task_id, reminder_date):
        self.task_id = task_id
        self.reminder_date = reminder_date

    @property
    def is_due(self):
        return datetime.now().date() >= self.reminder_date


def add_reminders(tasks):
    reminders = []
    for i, t in enumerate(tasks):
        date_str = input(f"Task {i+1} ({t['title']}): введите дату напоминания (YYYY-MM-DD) или 'none': ")
        if date_str.lower() == 'none':
            continue
        try:
            reminder_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            reminders.append(Reminder(t['id'], reminder_date))
        except ValueError as e:
            print(f"Ошибка даты: {e}")
    return reminders


def check_reminders(tasks, reminders):
    due_tasks = []
    for t in tasks:
        for r in reminders:
            if r.task_id == t['id'] and r.is_due:
                due_tasks.append((t, r.reminder_date))
    return due_tasks
