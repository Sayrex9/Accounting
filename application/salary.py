from datetime import datetime


def calculate_salary():
    """Рассчитывает зарплату"""
    current_date = datetime.now().strftime("%d.%m.%Y")
    print(f"[{current_date}] Выполняется расчет зарплаты...")
