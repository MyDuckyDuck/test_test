# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: DeskQueue
def dry_run(operation, data, dry_mode=False):
    if not dry_mode:
        return operation(data)
    print(f"[DRY-RUN] {operation.__name__}: {data}")
    return None
