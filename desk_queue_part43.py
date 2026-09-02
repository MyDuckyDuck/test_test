# === Stage 43: Добавь пагинацию длинных списков ===
# Project: DeskQueue
def paginate(tasks, page_size=20):
    """Compact paginator: yields (page_index, page_list) tuples."""
    for start in range(0, len(tasks), page_size):
        yield start // page_size, tasks[start:start + page_size]
