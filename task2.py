'''
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів 
на лотерейному квитку з числами, що випали випадковим чином і в 
певному діапазоні під час чергового тиражу. Наприклад, необхідно 
вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів, 
причому всі випадкові числа в наборі повинні бути унікальні.
'''
import random

def get_numbers_ticket(min, max, quantity):
    try:
        list_of_numbers = [i for i in range(min, max + 1)]
        list_of_numbers = random.sample(list_of_numbers, quantity)
        list_of_numbers.sort()
        print(list_of_numbers)
        return list_of_numbers
    except ValueError:
        print('Некоректно введено діапазон')
    except TypeError:
        print('Некоректний тип даних')

lottery_numbers = get_numbers_ticket(1, 64, 7)
