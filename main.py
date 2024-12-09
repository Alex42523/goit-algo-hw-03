from datetime import datetime
import random
def get_days_from_today(date):
    today = datetime.today()
    date = datetime.strptime(date, "%Y-%m-%d")
    a = today - date
    return a.days
print(get_days_from_today("2000-01-01"))
def get_numbers_ticket(min, max, quantity):
    if min >= 1 and min <= quantity <= max and max <= 1000:
        unique_numbers = random.sample(range(min, max + 1), quantity)
        return unique_numbers
    else: return []
print(get_numbers_ticket(1, 1000, 10))

