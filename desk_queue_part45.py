# === Stage 45: Добавь восстановление из резервной копии ===
# Project: DeskQueue
import pickle, os, sys

BACKUP_PATH = "deskqueue_backup.dat"

def save_backup(tasks, queues, statuses, labels):
    with open(BACKUP_PATH, "wb") as f:
        pickle.dump((tasks, queues, statuses, labels), f)
    print(f"[DeskQueue] Backup saved: {BACKUP_PATH} ({len(tasks)} tasks, {len(queues)} queues)")

def restore_backup():
    if not os.path.exists(BACKUP_PATH):
        print("[DeskQueue] No backup file found at:", BACKUP_PATH)
        return False
    try:
        with open(BACKUP_PATH, "rb") as f:
            tasks, queues, statuses, labels = pickle.load(f)
        print(f"[DeskQueue] Backup restored: {len(tasks)} tasks, {len(queues)} queues")
        return True
    except Exception as e:
        print(f"[DeskQueue] Backup restore failed: {e}")
        return False
