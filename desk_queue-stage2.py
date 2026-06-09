# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: DeskQueue
class Task:
    def __init__(self, title, description="", deadline=None, priority="medium", tags=None):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.tags = tags if tags else []
        self.status = "pending"

    def is_valid(self):
        if not self.title or len(self.title.strip()) < 2:
            return False, "Заголовок задачи должен быть не пустым и содержать минимум 2 символа."
        if self.deadline and self.deadline < datetime.now():
            return False, "Срок выполнения не может быть в прошлом."
        valid_priorities = {"low", "medium", "high"}
        if self.priority not in valid_priorities:
            return False, f"Приоритет должен быть одним из: {', '.join(valid_priorities)}."
        if not isinstance(self.tags, list):
            return False, "Метки должны быть списком строк."
        return True, None

def parse_user_input(raw_input):
    lines = raw_input.strip().split('\n')
    tasks = []
    for line in lines:
        if not line.strip():
            continue
        try:
            parts = line.split(' | ')
            title = parts[0].strip()
            deadline_str = parts[1].strip() if len(parts) > 1 else ""
            priority = parts[2].strip() if len(parts) > 2 else "medium"
            tags_str = parts[3].strip() if len(parts) > 3 else ""
            
            deadline = None
            if deadline_str:
                try:
                    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    deadline = None
            
            tags = [t.strip() for t in tags_str.split(',') if t.strip()]
            
            task = Task(title=title, description="", deadline=deadline, priority=priority, tags=tags)
            is_valid, error_msg = task.is_valid()
            if not is_valid:
                print(f"Ошибка валидации для задачи '{title}': {error_msg}")
                continue
            tasks.append(task)
        except Exception as e:
            print(f"Не удалось обработать строку ввода: {e}")
    return tasks
