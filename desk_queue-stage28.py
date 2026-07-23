# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: DeskQueue
def print_metrics(tasks, queues):
    """Print key project metrics."""
    total = len(tasks)
    if not tasks:
        return "No tasks yet."
    
    statuses = {}
    for t in tasks:
        s = t['status']
        statuses[s] = statuses.get(s, 0) + 1
    
    overdue = sum(1 for t in tasks if t.get('deadline') and datetime.datetime.now() > datetime.datetime.strptime(t['deadline'], '%Y-%m-%d %H:%M:%S'))
    
    print(f"Total tasks: {total}")
    print(f"By status:")
    for s, c in sorted(statuses.items()):
        print(f"  {s}: {c}")
    print(f"Overdue tasks: {overdue}")
