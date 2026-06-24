# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: DeskQueue
def load_tasks_from_json(filepath: str) -> list[dict]:
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив задач")
        valid_tasks = []
        for idx, item in enumerate(data):
            try:
                task_id = str(item.get('id', f"task_{idx}"))
                title = str(item.get('title', 'Без названия'))
                status = str(item.get('status', 'new')).lower()
                deadline = item.get('deadline')
                tags = set(str(t).strip() for t in item.get('tags', [])) if isinstance(item.get('tags'), list) else set()
                valid_tasks.append({
                    "id": task_id,
                    "title": title,
                    "status": status,
                    "deadline": deadline,
                    "tags": tags
                })
            except Exception:
                continue
        return valid_tasks
    except FileNotFoundError:
        print(f"Файл {filepath} не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return []
