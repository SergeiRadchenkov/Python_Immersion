'''
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
'''
import random

number = [1, 1, 2, 2, 2, 3, 4, 5, 8, 9, 9, 10, 10, 10, 10]
random.shuffle(number)
for item in number:
    if (count := number.count(item)) >= 2:
        for _ in range(count//2):
            number.remove(item)
            number.remove(item)
print(number)

