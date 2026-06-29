# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: DeskQueue
def generate_monthly_stats(tasks, year=2024):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'completed': 0, 'overdue': 0})
    for task in tasks:
        if not isinstance(task['created_at'], str) or len(task['created_at']) < 7: continue
        month_key = f"{year}-{task['created_at'][:6]}"
        stats[month_key]['total'] += 1
        if task.get('status') == 'completed': stats[month_key]['completed'] += 1
        deadline = task.get('deadline', '')
        if deadline and len(deadline) >= 7:
            try:
                d_date = datetime.strptime(deadline[:4] + '-' + deadline[5:7], '%Y-%m')
                if d_date < datetime.now().replace(day=1): stats[month_key]['overdue'] += 1
            except ValueError: pass
    return dict(sorted(stats.items()))
