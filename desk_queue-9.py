# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: DeskQueue
import json, sys, os
from datetime import datetime, timedelta
if len(sys.argv) > 1:
    data = json.loads(sys.argv[1])
else:
    with open('initial_data.json') as f:
        data = json.load(f)
data['created_at'] = datetime.utcnow().isoformat() + 'Z'
for task in data.get('tasks', []):
    if not task.get('deadline'):
        deadline_str = (datetime.utcnow() + timedelta(hours=24)).isoformat() + 'Z'
        task['deadline'] = deadline_str
if os.path.exists('initial_data.json'):
    with open('initial_data.json') as f:
        initial_content = json.load(f)
    if not data.get('tasks'):
        data.update(initial_content)
with open('desk_queue_db.json', 'w') as f:
    json.dump(data, f, indent=2)
