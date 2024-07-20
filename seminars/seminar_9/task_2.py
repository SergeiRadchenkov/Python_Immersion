'''
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
'''
import random as rnd
from typing import Callable
from functools import wraps


def decor(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if a not in range(1, 101):
            print(f'Введённое число {a} недопустимо, будем играть по моим правилам!')
            a = rnd.randint(1, 100)
        if b not in range(1, 11):
            print(f'Введённое число {b} недопустимо, будем играть по моим правилам!')
            b = rnd.randint(1, 10)
        return func(a, b)


    return wrapper


@decor
def inner(a: int, b: int):
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


inner(202, 6)