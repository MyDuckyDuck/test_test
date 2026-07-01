# === Stage 17: Добавь группировку записей по категориям ===
# Project: DeskQueue
def group_tasks_by_category(tasks):
    groups = {}
    for task in tasks:
        cat = task.get('category', 'general')
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(task)
    return groups
