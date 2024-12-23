import random
from datetime import datetime
def get_days_from_today(date):
    today = datetime.today()
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Невірний тип дати")
        return ""
    a = today - date
    return a.days
print(get_days_from_today("2021-109"))
print(get_days_from_today("2021-10-09"))
def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and min <= quantity <= max:
        numbers = set()
        while len(numbers) <= quantity:
            number = random.randint(min, max)
            numbers.add(number)
        return sorted(list(numbers))
    else:
        return "Числа вибрані невірно"
print(get_numbers_ticket(1, 100, 101))
print(get_numbers_ticket(1, 100, 10))
