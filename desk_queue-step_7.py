# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: DeskQueue
def sort_tasks(tasks, key='date'):
    if not tasks: return tasks
    reverse = {'priority': True, 'name': False}.get(key, False)
    def _sort_key(t):
        val = t.get('due_date', 0)
        try: val += int(t.get('priority', 3)) * -10000
        except: pass
        return (val if key == 'date' else (t['name'] or ''), reverse)
    return sorted(tasks, key=_sort_key)
