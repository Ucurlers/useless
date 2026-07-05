# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: SupportQueue
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return {item['id']: item for item in data}
        elif isinstance(data, dict):
            return data
        else:
            raise ValueError("Неверный формат данных JSON")
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}
    except KeyError as e:
        print(f"Отсутствует ключ в данных: {e}")
        return {}
