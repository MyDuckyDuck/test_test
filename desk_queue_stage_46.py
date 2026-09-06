# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: DeskQueue
import json, datetime, uuid, random

def migrate_to_v5():
    """Migrate DeskQueue data structure to version 5.
    
    Changes:
    - Adds 'priority' field (1-5) to Task class
    - Adds 'tags' list to Task class  
    - Adds 'created_at' timestamp to Task class
    - Adds 'completed_at' timestamp to Task class
    - Adds 'deadline' field to Task class
    - Adds 'status' field to Task class
    - Adds 'id' field to Task class
    - Adds 'queue_name' field to Task class
    - Adds 'assignee' field to Task class
    - Adds 'source' field to Task class
    - Adds 'metadata' dict to Task class
    - Adds 'version' field to Queue class
    - Adds 'created_at' timestamp to Queue class
    - Adds 'config' dict to Queue class
    """
    
    # Define the new Task structure
    task_schema = {
        'id': str(uuid.uuid4()),
        'queue_name': str,
        'status': str,
        'priority': int,
        'tags': list,
        'created_at': datetime.datetime,
        'deadline': datetime.datetime,
        'completed_at': datetime.datetime,
        'assignee': str,
        'source': str,
        'metadata': dict
    }
    
    # Define the new Queue structure
    queue_schema = {
        'name': str,
        'version': int,
        'created_at': datetime.datetime,
        'config': dict
    }
    
    # Version info
    version_info = {
        'version': 5,
        'description': 'Added priority, tags, timestamps, and metadata',
        'migration_date': datetime.datetime.now().isoformat(),
        'changelog': [
            'Added priority field (1-5) to Task',
            'Added tags list to Task',
            'Added created_at to Task',
            'Added deadline to Task',
            'Added completed_at to Task',
            'Added status to Task',
            'Added id to Task',
            'Added queue_name to Task',
            'Added assignee to Task',
            'Added source to Task',
            'Added metadata dict to Task',
            'Added version to Queue',
            'Added created_at to Queue',
            'Added config to Queue'
        ]
    }
    
    return task_schema, queue_schema, version_info
