'''
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
'''
print(*(x for x in range(0, 101, 2) if sum(map(int, str(x))) != 8))

# Вариант 2
print(*(x for x in range(0, 101, 2) if x // 10 + x % 10 != 8))
