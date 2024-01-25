'''
Створіть функцію get_days_from_today(date), яка розраховує 
кількість днів між заданою датою і поточною датою.
'''
from datetime import datetime

def get_days_from_today(date):
    try:
        date = date.replace(' ', '-')
        date_not_str = datetime.strptime(date, '%Y-%m-%d')
        today_date = datetime.today()
        difference_date = today_date - date_not_str
        difference_days = difference_date.days
        print(f'Різниця у днях між {date} та сьогодні: {difference_days} днів')
        return difference_days
    except ValueError:
        print(f'Неправильний формат дати')

input_date = input('Введіть будь-яку дату у форматі YYYY MM DD: ')    
get_days_from_today(input_date)