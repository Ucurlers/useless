# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: SupportQueue
def validate_datetime(value):
    """Validates and parses a datetime string in YYYY-MM-DD format."""
    if not isinstance(value, str) or len(value.split('-')) != 3:
        raise ValueError(f"Некорректная дата: '{value}'. Ожидается формат YYYY-MM-DD.")
    year, month, day = value.split('-')
    try:
        year_int, month_int, day_int = int(year), int(month), int(day)
    except ValueError:
        raise ValueError(f"Некорректная дата: '{value}'. Не все части — числа.")
    if not (1 <= month_int <= 12 and 1 <= day_int <= 31):
        raise ValueError(f"Некорректная дата: '{value}'. Месяц и день вне диапазона.")
    import datetime as dt
    try:
        dt.datetime(year_int, month_int, day_int)
    except ValueError:
        raise ValueError(f"Некорректная дата: '{value}'. Такой даты не существует (например 2024-02-30).")
    return f"{year}-{month}-{day}"

def format_error_message(error):
    """Formats error messages for user-friendly output."""
    if isinstance(error, ValueError):
        return str(error)
    elif isinstance(error, TypeError):
        return "Ошибка: Некорректный тип данных. Ожидаются строки и числа."
    else:
        return f"Неизвестная ошибка: {str(error)}"

def process_support_request(request_data):
    """Processes a support request with validation."""
    try:
        priority = validate_datetime(request_data.get('priority_date')) if 'priority_date' in request_data else "2024-01-01"
        description = str(request_data.get('description', ''))
        if not description.strip():
            raise ValueError("Описание обращения не может быть пустым.")
        return {"status": "success", "message": f"Обращение обработано успешно.", "priority_date": priority, "description": description}
    except Exception as e:
        return {"status": "error", "message": format_error_message(e)}

# Пример использования
request = {
    'priority_date': '2024-13-45',
    'description': 'Тестовое обращение'
}
result = process_support_request(request)
print(result)
