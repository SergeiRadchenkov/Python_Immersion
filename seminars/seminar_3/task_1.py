'''
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
'''
number = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6]
new_number = []
for i in number:
    if i not in new_number:
        new_number.append(i)
print(new_number)

print()
# Вариант 2
import random

print(nums := [random.randint(0, 10) for _ in range(20)])
print(list(set(nums)))
