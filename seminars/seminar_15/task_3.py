'''
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат
'''
from typing import Callable
from functools import wraps
import logging


def decor(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        form = '{levelname:<5} - {asctime:<5} - {funcName} - {msg}'
        logging.basicConfig(filename='mylog.log', filemode='a', encoding='utf-8', level=logging.INFO,
                            style='{', format=form)

        result = func(*args, **kwargs)
        str_args, str_kwargs = '', ''
        if args:
            str_args = ('args: ' + ','.join(args)) or ''
        if kwargs:
            str_kwargs = ('kwargs: ' + ','.join([f'{key}={value}' for key, value in kwargs.items()])) or ''
        logger.info(msg=f'result: {result}, {str_args}' + (', ' if str_args and str_kwargs else '') + f'{str_kwargs}')
        return result
    return wrapper


@decor
def some_func(a: str, b: str):
    return a + '_' + b


some_func('Первая', 'Вторая')
some_func(b='три', a='asdasd')
some_func('три', b='asdasd')
