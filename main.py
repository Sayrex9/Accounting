import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print(
        f"Программа «Бухгалтерия» запущена. Текущая дата и время: {current_date}")

    calculate_salary()
    get_employees()
