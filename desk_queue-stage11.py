# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: DeskQueue
import json, os

def save_tasks(tasks_file='tasks.json'):
    if not os.path.exists(tasks_file):
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)
    try:
        with open(tasks_file, 'r+', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            tasks = json.loads(content)
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
        return tasks
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return []

def load_tasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
