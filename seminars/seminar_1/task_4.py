'''
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
'''

# Вариант 1
row = int(input('Введите количество рядов: '))
k = row
j = 1
for _ in range(row):
    print(' ' * (k - 1), '*' * j, sep='')
    k -= 1
    j += 2

# Вариант 2
height = int(input('Введите высоту ёлки: '))
for row in range(height):
    print(f'{"*" * (2 * row + 1):^{height*2 + 1}}')
