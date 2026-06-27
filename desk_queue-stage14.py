# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: DeskQueue
def generate_summary(tasks):
    if not tasks:
        print("Нет данных для сводки.")
        return
    
    statuses = {}
    queues = set()
    today = datetime.date.today()
    
    for task in tasks:
        status = task.get('status', 'unknown')
        queue = task.get('queue', 'general')
        
        if status not in statuses:
            statuses[status] = 0
        statuses[status] += 1
        
        queues.add(queue)
        
        deadline = task.get('deadline')
        if isinstance(deadline, str):
            try:
                d_date = datetime.strptime(deadline[:10], '%Y-%m-%d').date()
                days_left = (d_date - today).days
                if days_left < 0:
                    print(f"⚠️ Задача '{task.get('id')}' просрочена на {abs(days_left)} дней.")
            except ValueError:
                pass
    
    print("\n📊 Сводка по задачам:")
    for status, count in sorted(statuses.items()):
        print(f"  Статус '{status}': {count} задача(й)")
    
    if queues:
        print(f"\n🗂 Очереди: {', '.join(sorted(queues))}")
