# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: DeskQueue
def filter_tasks(status=None, category=None, tags=None):
    filtered = []
    for task in tasks:
        if status and task['status'] != status: continue
        if category and task.get('category') != category: continue
        if tags is not None:
            task_tags = set(task.get('tags', []))
            if tags and not any(t in task_tags for t in tags): continue
        filtered.append(task)
    return filtered

def search_tasks(query=None, status=None, limit=10):
    results = filter_tasks(status=status)
    if query:
        q_lower = query.lower()
        results = [t for t in results if any(q_lower in str(v).lower() for v in t.values())]
    return results[:limit]

def get_task_summary():
    total = len(tasks)
    by_status = {}
    for task in tasks:
        s = task['status']
        by_status[s] = by_status.get(s, 0) + 1
    categories = set(t.get('category') for t in tasks if t.get('category'))
    tags_set = set(tag for t in tasks for tag in t.get('tags', []))
    return {'total': total, 'by_status': by_status, 'categories': list(categories), 'unique_tags': sorted(list(tags_set))}
