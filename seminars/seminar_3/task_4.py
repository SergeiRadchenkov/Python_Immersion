'''
Создайте вручную список с повторяющимися целыми числами.
Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
Нумерация начинается с единицы.
'''
import random

print(lst := [random.randint(0, 10) for _ in range(20)])

for i in range(len(lst)):
    if lst[i] % 2 != 0:
        print(i+1, end=' ')

# Вариант 2
lst = [1, 1, 2, 2, 3, 3, 4, 'str', None, None]

my_set = set(lst)
for item in my_set:
    if lst.count(item) == 2:
        while item in lst:
            lst.remove(item)
print(lst)