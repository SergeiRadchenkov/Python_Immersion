'''
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
'''
from typing import Callable
import json
import os
from functools import wraps


def decor(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = func.__name__ + '.json'

        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
        else:
            data = dict()

        result = func(*args, **kwargs)
        data[result.__repr__()] = list(args + tuple(kwargs.items()))

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return result

    return wrapper


@decor
def some_func(a: str, b: str):
    return a + '_' + b


some_func('Первая', 'Вторая')
some_func(b='три', a='asdasd')
some_func('три', b='asdasd')
