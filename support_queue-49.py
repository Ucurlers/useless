# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: SupportQueue
def self_check():
    print("=" * 60)
    print("  Финальная самопроверка SupportQueue")
    print("=" * 60)
    errors = []
    if not queue:
        errors.append("Очередь пуста")
    else:
        print(f"✓ Очередь содержит {len(queue)} обращений")
        for ticket in queue:
            print(f"  - #{ticket['id']} [{ticket['priority']}] от {ticket['user']}")
            if ticket['status'] == 'new':
                print(f"    -> Ожидает исполнителя")
    if not tickets:
        errors.append("Справочник исполнителей пуст")
    else:
        print(f"✓ Исполнителей: {len(tickets)}")
    if not history:
        errors.append("История ответов пуста")
    else:
        print(f"✓ Записей в истории: {len(history)}")
    if errors:
        print("\n⚠ Ошибки:")
        for e in errors:
            print(f"  ✗ {e}")
        return False
    print("\n✅ Приложение полностью готово!")
    return True
