# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: DeskQueue
import shutil
import os
from datetime import datetime

def backup_data_file(data_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    if not os.path.exists(data_path):
        return None
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(data_path)}")
    shutil.copy2(data_path, backup_path)
    return backup_path
