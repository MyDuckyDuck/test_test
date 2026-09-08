# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: DeskQueue
def demo():
    print("=" * 60)
    print("DESKQUEUE — Демонстрация пользовательского сценария")
    print("=" * 60)

    # Создаём задачу
    task = Task(
        title="Обработать отчёт по продажам",
        deadline=timedelta(days=2),
        priority=1,
        status=Status.PENDING,
        tags={"sales", "quarterly"},
    )

    # Добавляем задачу в очередь
    queue = Queue(name="sales_queue", capacity=10)
    queue.add(task)
    print(f"✅ Добавлена задача в очередь '{queue.name}'")
    print(f"   Статус: {task.status.value}")
    print(f"   Срок: {task.deadline}")
    print(f"   Метки: {', '.join(task.tags)}")
    print(f"   Очередь: {queue.count} / {queue.capacity}")

    # Обновляем статус
    task.status = Status.IN_PROGRESS
    print(f"\n🔄 Статус изменён: {task.status.value}")

    # Проверяем, можно ли добавить ещё задачу
    new_task = Task(title="Тестовая задача", deadline=timedelta(days=1))
    if queue.full():
        print("⛔ Очередь переполнена, задача не добавлена")
    else:
        queue.add(new_task)
        print(f"✅ Добавлена задача: '{new_task.title}'")

    # Показываем все задачи в очереди
    print(f"\n📋 Все задачи в очереди '{queue.name}':")
    for t in queue.tasks:
        print(f"   - {t.title} [{t.status.value}]")

    # Удаляем задачу
    queue.remove(task)
    print(f"\n🗑️ Удалена задача: '{task.title}'")
    print(f"   Очередь теперь: {queue.count} / {queue.capacity}")

    # Создаём новый менеджер и добавляем очередь
    manager = DeskQueueManager()
    manager.add_queue(queue)
    print(f"\n📊 Менеджер очередей: {manager.count} очередь(ей)")
    print(f"   Очереди: {', '.join(q.name for q in manager.queues)}")

    # Проверяем, что очередь не пуста
    if not queue.empty():
        print("⚠️ Очередь не пуста, хотя мы удалили задачу")
    else:
        print("✅ Очередь пуста, всё работает корректно")

    print("\n" + "=" * 60)
    print("Демонстрация завершена")
    print("=" * 60)
