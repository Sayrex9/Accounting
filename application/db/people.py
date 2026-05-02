from datetime import datetime


def get_employees():
    """Получает данные о сотруднике"""
    current_date = datetime.now().strftime("%d.%m.%Y")
    print(f"[{current_date}] Получаю данные о сотруднике...")
