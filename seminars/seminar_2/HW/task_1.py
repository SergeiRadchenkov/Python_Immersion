'''
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''
num = 255
base = 16
res = ''
hex_digits = "0123456789ABCDEF"
num2 = hex(num)

while num:
    remainder = num % base
    res = hex_digits[remainder] + res
    num //= base

print(f'Шестнадцатеричное представление числа: {res}')
print(f'Проверка результата: {num2}')