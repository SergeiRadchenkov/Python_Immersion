'''
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
'''
import random as rnd


def outer():
    a = rnd.randint(1, 101)
    b = rnd.randint(1, 11)
    def inner():
        nonlocal a, b
        print(f'У тебя {b} попыток угадать число!')
        while b:
            guess = int(input('Введи число: '))
            if guess > a:
                print(f'Загаданное число меньше, чем {guess}')
            elif guess < a:
                print(f'Загаданное число больше, чем {guess}')
            else:
                print(f'Ты угадал! Было загадано {a}')
                break
            b -= 1
        else:
            print('У тебя закончились попытки')

    return inner


primer = outer()
primer()
