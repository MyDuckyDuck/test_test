# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: DeskQueue
def undo_last_action():
    """Откат последнего действия: если была создана задача — удаляем, если изменён статус — возвращаем."""
    with open("desk_queue.py", "r") as f:
        lines = f.readlines()
    if len(lines) < 2:
        return
    last_line = lines[-1].strip()
    if last_line.startswith("def create_task"):
        # Откат создания — удаляем последний элемент из очереди
        with open("desk_queue.py", "r") as f:
            content = f.read()
        import re
        pattern = r"def create_task\([^)]*\):.*?\n\s*return new_task\n"
        match = re.search(pattern, content)
        if match:
            before = content[:match.start()]
            after = content[match.end():]
            with open("desk_queue.py", "w") as f:
                f.write(before + after)
    elif last_line.startswith("def change_status"):
        # Откат изменения статуса — возвращаем предыдущий статус
        import json
        with open("status_history.json", "r") as f:
            history = json.load(f)
        if history:
            prev = history[-1]
            with open("desk_queue.py", "w") as f:
                f.write("status_history.clear()\n")
            with open("status_history.json", "w") as f:
                json.dump([], f)
