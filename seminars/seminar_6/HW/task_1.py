'''
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна)
или "False" (дата некорректна) в зависимости от результата проверки.
'''

date_to_prove = '15.4.2023'
date_to_prove = '0.5.2022'
date_to_prove = '12.0.2022'
date_to_prove = '12.5.-2022'
date_to_prove = '12.13.2022'

def date_task(dates):
    dat, mon, yea = map(int, dates.split('.'))
    if mon == 2:
        if (yea % 4 == 0 and yea % 100 != 0) or (yea % 400 == 0):
            if dat <= 29 and dat > 0:
                return True
            else:
                return False
        else:
            if dat <= 28 and dat > 0:
                return True
            else:
                return False
    elif mon in [4, 6, 9, 11]:
        if dat <= 30 and dat > 0:
            return True
        else:
            return False
    else:
        if dat <= 31 and dat > 0 and mon > 0 and yea > 0 and mon <= 12:
            return True
        else:
            return False

print(date_task(date_to_prove))

# Вариант 2
from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))

