# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: DeskQueue
def show_menu():
    print("\n=== Мен DeskQueue ===")
    print("1. Добавить задачу в очередь")
    print("2. Показать все задачи")
    print("3. Изменить статус задачи")
    print("4. Удалить задачу по ID")
    print("5. Фильтровать задачи по метке")
    print("6. Выход")
    cmd = input("Выберите действие (1-6): ")
    if cmd == "1":
        task_id = int(input("ID задачи: "))
        title = input("Название: ")
        deadline = input("Срок (YYYY-MM-DD HH:MM): ")
        status = input("Статус (new, in_progress, done): ").strip() or "new"
        tags = input("Метки через запятую: ").split(",") if input("Добавить метки? (y/n): ").lower() == 'y' else []
        tasks[task_id] = {"title": title, "deadline": deadline, "status": status, "tags": tags}
    elif cmd == "2":
        for tid, t in sorted(tasks.items()):
            print(f"[{tid}] {t['title']} | Статус: {t['status']} | Срок: {t['deadline']} | Метки: {', '.join(t['tags'])}")
    elif cmd == "3":
        tid = int(input("ID задачи для изменения статуса: "))
        if tid in tasks:
            new_status = input("Новый статус (new, in_progress, done): ").strip() or "in_progress"
            tasks[tid]["status"] = new_status
    elif cmd == "4":
        try:
            del_tasks = int(input("ID задачи для удаления: "))
            if del_tasks in tasks:
                del tasks[del_tasks]
                print("Задача удалена.")
            else:
                print("Задача не найдена.")
        except ValueError:
            print("Неверный ID.")
    elif cmd == "5":
        tag = input("Введите метку для фильтрации: ").strip() or None
        if tag:
            filtered = [tid for tid, t in tasks.items() if tag.lower() in [t.get('tag', '').lower() for t in tasks.values()] and any(tag.lower() == tg.lower() for tg in tasks[tid].get('tags', []))]
            # Исправление логики фильтрации: перебираем задачи и проверяем метку
            filtered = [(tid, t) for tid, t in tasks.items() if tag.lower() in [tg.lower() for tg in t.get("tags", [])]]
            print(f"Задачи с меткой '{tag}':")
            for tid, t in sorted(filtered):
                print(f"[{tid}] {t['title']} | Статус: {t['status']}")
        else:
            print("Введите корректную метку.")
    elif cmd == "6":
        print("Выход из системы.")
        return False
    input("\nНажмите Enter для продолжения...")
    return True
