# === Stage 20: Добавь восстановление записей из архива ===
# Project: DeskQueue
def restore_from_archive(archive_path: str) -> list[Task]:
    """Восстанавливает задачи из текстового архива DeskQueueArchive."""
    archive = DeskQueueArchive.from_file(archive_path)
    return [
        Task(
            id=t["id"],
            queue=t.get("queue", "default"),
            deadline=datetime.fromisoformat(t["deadline"]),
            priority=int(t["priority"]),
            label=t.get("label", ""),
        )
        for t in archive.tasks
    ]
