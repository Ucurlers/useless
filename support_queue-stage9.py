# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: SupportQueue
import json, random, uuid

INITIAL_DATA = '''
{
  "agents": [
    {"id": "agent_01", "name": "Анна Петрова", "status": "online"},
    {"id": "agent_02", "name": "Иван Сидоров", "status": "busy"}
  ],
  "tickets": [
    {
      "id": "T-1001",
      "subject": "Ошибка входа в систему",
      "priority": 1,
      "assignee_id": null,
      "history": []
    },
    {
      "id": "T-1002",
      "subject": "Вопрос по тарифам",
      "priority": 3,
      "assignee_id": "agent_01",
      "status": "in_progress",
      "history": [
        {"role": "user", "text": "Здравствуйте, подскажите стоимость расширенной лицензии.", "timestamp": "2024-01-15T10:30:00Z"},
        {"role": "agent", "text": "Добрый день. Расширенная лицензия стоит 5000 руб/мес.", "timestamp": "2024-01-15T10:35:00Z"}
      ]
    }
  ],
  "config": {
    "max_queue_size": 100,
    "default_priority": 5
  }
}'''

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        return {
            "agents": [a.copy() for a in data.get("agents", [])],
            "tickets": [t.copy() for t in data.get("tickets", [])],
            "config": data.get("config", {"max_queue_size": 100, "default_priority": 5})
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON данных поддержки: {e}")
        return None

if __name__ == "__main__":
    loaded_data = load_initial_data(INITIAL_DATA)
    if loaded_data:
        print(f"Загружено агентов: {len(loaded_data['agents'])}, заявок: {len(loaded_data['tickets'])}")
