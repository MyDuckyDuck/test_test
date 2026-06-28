# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: DeskQueue
def calculate_weekly_stats(tasks):
    from datetime import date, timedelta
    if not tasks: return {}
    stats = {}
    for task in tasks:
        d = date.fromisoformat(task['date'])
        week_start = (d - timedelta(days=d.weekday())).isoformat()
        key = f"{task.get('queue', 'general')}|{week_start}"
        if key not in stats: stats[key] = {'count': 0, 'overdue': 0}
        stats[key]['count'] += 1
        deadline = date.fromisoformat(task['deadline'])
        if task['status'] != 'completed' and d >= deadline: stats[key]['overdue'] += 1
    return stats
