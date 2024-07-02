'''
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
'''
num = int(input('Введите целое число: '))
base = int(input('Введите систему исчисления: '))

original_number = num
result = ''
while num:
    result = str(num % base) + result
    num //= base

print(f'Число {original_number} в {base}-ичной системе исчисления будет: {result}')
print(bin(original_number)[2:] if base == 2 else oct(original_number)[2:])