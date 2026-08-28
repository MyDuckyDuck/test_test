# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: DeskQueue
import sys
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="DeskQueue CLI")
    parser.add_argument("action", choices=["add", "list", "show", "update", "delete"], help="Операция")
    parser.add_argument("--id", help="ID задачи (для show/update/delete)")
    parser.add_argument("--title", help="Заголовок задачи")
    parser.add_argument("--queue", help="Очередь задачи")
    parser.add_argument("--deadline", help="Срок задачи (YYYY-MM-DD)")
    parser.add_argument("--status", help="Статус задачи")
    parser.add_argument("--tags", help="Метки задачи через запятую")
    args = parser.parse_args()

    if args.action == "add":
        print("Добавление задачи...")
    elif args.action == "list":
        print("Список задач...")
    elif args.action == "show":
        if not args.id:
            print("Укажите --id")
            sys.exit(1)
        print(f"Показ задач с ID: {args.id}")
    elif args.action == "update":
        if not args.id:
            print("Укажите --id")
            sys.exit(1)
        print(f"Обновление задачи {args.id}...")
    elif args.action == "delete":
        if not args.id:
            print("Укажите --id")
            sys.exit(1)
        print(f"Удаление задачи {args.id}...")

if __name__ == "__main__":
    main()
