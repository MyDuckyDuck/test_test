# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: DeskQueue
def print_task_table(tasks):
    if not tasks:
        print("Нет задач.")
        return
    header = f"{'ID':<5} {'Статус':<10} {'Срок':<12} {'Приоритет':<8} {'Метка':<15}"
    print(header)
    print("-" * len(header))
    for t in tasks:
        priority = "HIGH" if t.priority == 3 else ("MED" if t.priority == 2 else "LOW")
        deadline_str = str(t.deadline) if t.deadline else "-"
        label = f"{t.label}"[:14]
        print(f"{t.id:<5} {t.status.name:<10} {deadline_str:<12} {priority:<8} {label}")

def print_queue_table(queue, tasks):
    if not queue.tasks:
        print(f"Очередь '{queue.name}' пуста.")
        return
    header = f"{'ID':<5} {'Статус':<10} {'Срок':<12} {'Приоритет':<8} {'Метка':<15}"
    print(header)
    print("-" * len(header))
    for t in queue.tasks:
        priority = "HIGH" if t.priority == 3 else ("MED" if t.priority == 2 else "LOW")
        deadline_str = str(t.deadline) if t.deadline else "-"
        label = f"{t.label}"[:14]
        print(f"{t.id:<5} {t.status.name:<10} {deadline_str:<12} {priority:<8} {label}")
