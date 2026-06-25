# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: DeskQueue
def search_tasks(query, fields=None):
    if not query:
        return tasks_list.copy()
    query_lower = query.lower().strip()
    if fields is None:
        fields = ['id', 'title', 'description', 'status', 'priority', 'tags']
    results = []
    for task in tasks_list:
        match_found = False
        for field_name in fields:
            value = getattr(task, field_name, '')
            if isinstance(value, str):
                if query_lower in value.lower():
                    match_found = True
                    break
            elif isinstance(value, list) and any(query_lower in item.lower() for item in value):
                match_found = True
                break
        if match_found:
            results.append(task)
    return results
