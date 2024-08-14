import logging

logging.basicConfig(level=logging.NOTSET)
logging.debug('Очень подробная информация. Заменяем множество "принтов"')
logging.info('Немного информации о работе кода')
logging.warning('Внимание! Надвигается буря!')
logging.error('Поймали ошибку. Дальше только неизветность')
logging.critical('На этом всё')
