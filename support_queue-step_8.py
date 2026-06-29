# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SupportQueue
def print_menu():
    print("\n=== Меню системы поддержки ===")
    print("1. Добавить обращение в очередь")
    print("2. Выдать задачу исполнителю")
    print("3. Просмотреть историю ответов")
    print("4. Выход")
    try:
        choice = input("Выберите действие (1-4): ").strip()
        return choice
    except EOFError:
        return "exit"

if __name__ == "__main__":
    while True:
        action = print_menu()
        if action in ["1", "2", "3"]:
            print("Функционал будет реализован в следующих этапах.")
        elif action == "4":
            print("Завершение работы системы.")
            break
