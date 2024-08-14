'''
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
'''
from typing import Callable
from functools import wraps
import logging


def decor(func: Callable) -> Callable:
    logger = logging.getLogger(__name__)
    form = '{msg}'
    logging.basicConfig(filename='mylog.log', filemode='a', encoding='utf-8', level=logging.INFO,
                        style='{', format=form)
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        str_args, str_kwargs = '', ''
        if args:
            str_args = ('args: ' + ','.join(args)) or ''
        if kwargs:
            str_kwargs = ('kwargs: ' + ','.join([f'{key}={value}' for key, value in kwargs.items()])) or ''
        logging.info(msg=f'result: {result}, {str_args}' + (', ' if str_args and str_kwargs else '') + f'{str_kwargs}')
        return result
    return wrapper


@decor
def some_func(a: str, b: str):
    return a + '_' + b


some_func('Первая', 'Вторая')
some_func(b='три', a='asdasd')
some_func('три', b='asdasd')
