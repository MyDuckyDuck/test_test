# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: DeskQueue
def validate_date(date_str):
    """Парсит дату 'YYYY-MM-DD', возвращает datetime.date или None."""
    if not date_str:
        return None
    parts = date_str.strip().split('-')
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        return None
    try:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        d = datetime.date(year, month, day)
        if d.year == year and d.month == month and d.day == day:
            return d
        return None
    except ValueError:
        return None

def format_error(message):
    """Форматирует сообщение об ошибке."""
    return f"[DeskQueue Error] {message}"

class DeskError(Exception):
    pass
