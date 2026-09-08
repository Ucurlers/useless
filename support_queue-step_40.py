# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: SupportQueue
import argparse

def main():
    parser = argparse.ArgumentParser(description="SupportQueue CLI")
    parser.add_argument("action", choices=["new", "list", "assign", "reply", "history"],
                        help="Операция: new, list, assign, reply, history")
    parser.add_argument("--id", "-i", type=int, help="ID обращения (для assign/reply/history)")
    parser.add_argument("--priority", "-p", choices=["low", "medium", "high"],
                        help="Приоритет (для new)")
    parser.add_argument("--agent", "-a", help="Имя исполнителя (для assign)")
    parser.add_argument("--subject", "-s", help="Тема обращения (для new)")
    parser.add_argument("--message", "-m", help="Сообщение (для reply)")
    args = parser.parse_args()
    print(f"Action: {args.action}, ID: {args.id}, Priority: {args.priority}, Agent: {args.agent}, Subject: {args.subject}, Message: {args.message}")

if __name__ == "__main__":
    main()
