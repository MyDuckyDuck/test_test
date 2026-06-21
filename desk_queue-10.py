# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: DeskQueue
def export_state_to_json():
    import json
    from datetime import datetime
    
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "queues": {},
        "tasks": []
    }
    
    for queue_name, tasks in _queue_registry.items():
        if not tasks:
            continue
        
        q_state = {
            "name": queue_name,
            "task_count": len(tasks),
            "total_priority": sum(t.priority for t in tasks),
            "oldest_deadline": min((t.deadline for t in tasks if t.deadline is not None), default=None)
        }
        
        # Сортировка задач внутри очереди по дедлайну, затем по приоритету
        sorted_tasks = sorted(tasks, key=lambda x: (x.deadline or datetime.max.timestamp(), -x.priority))
        
        for task in sorted_tasks:
            q_state["tasks"].append({
                "id": task.id,
                "title": task.title,
                "status": task.status.value if hasattr(task.status, 'value') else str(task.status),
                "priority": task.priority,
                "deadline": task.deadline.isoformat() if task.deadline else None,
                "tags": list(task.tags) if hasattr(task.tags, '__iter__') and not isinstance(task.tags, str) else []
            })
        
        state["queues"][queue_name] = q_state
    
    # Добавляем глобальную статистику
    stats = {
        "total_tasks": sum(len(t) for t in _queue_registry.values()),
        "completed_count": sum(1 for tasks in _queue_registry.values() for t in tasks if t.status == 'done'),
        "in_progress_count": sum(1 for tasks in _queue_registry.values() for t in tasks if t.status == 'processing')
    }
    
    state["stats"] = stats
    
    return json.dumps(state, indent=2)
