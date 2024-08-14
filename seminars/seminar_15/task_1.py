'''
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
'''
import logging

logger = logging.getLogger(__name__)
form = '{asctime:<20} - {levelname:<10} - {msg}'

logging.basicConfig(filename='mylog.log', filemode='w', encoding='utf-8', level=logging.ERROR,
                   style='{',  format=form)


def func(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logger.error(msg=e)


func(100, 0)
