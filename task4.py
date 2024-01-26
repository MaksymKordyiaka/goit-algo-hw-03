'''
У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, 
яка допоможе вам визначати, кого з колег потрібно привітати.

У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача 
та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція 
також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.
'''
import datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "Oleksiy Kuchkin", "birthday": "1995.01.28"},
    {"name": "Andruha Somov", "birthday": "1994.02.2"},
]

def get_upcoming_birthdays(users):
    today = dtdt.today().date()
    birthdays = []
    for user in users:
        birth_date = user['birthday']
        birth_date = str(today.year) + birth_date[4:]
        birth_date = dtdt.strptime(birth_date, '%Y.%m.%d').date()
        week_day = birth_date.isoweekday()
        difference_date = (birth_date - today).days
        if 0 <= difference_date <= 7:
            if week_day < 6: 
                birthdays.append({'name':user['name'], 'birthday':birth_date.strftime('%Y.%m.%d')})
            elif week_day == 6:
                birthdays.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=2)).strftime('%Y.%m.%d')})
            else:
                birthdays.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=1)).strftime('%Y.%m.%d')})      
    return birthdays
print(get_upcoming_birthdays(users))
