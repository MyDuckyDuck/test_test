# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: DeskQueue
def switch_profile(new_name):
    """Переключение активного профиля."""
    global current_user
    if new_name in users:
        current_user = new_name
        print(f"✅ Профиль переключен на {new_name}")
    else:
        print(f"❌ Профиль '{new_name}' не найден.")
