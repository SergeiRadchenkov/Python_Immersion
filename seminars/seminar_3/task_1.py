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