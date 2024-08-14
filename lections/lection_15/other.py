import logging

logger = logging.getLogger(__name__)


def log_all():
    logger.debug('Очень подробная информация. Заменяем множество "принтов"')
    logger.info('Немного информации о работе кода')
    logger.warning('Внимание! Надвигается буря!')
    logger.error('Поймали ошибку. Дальше только неизветность')
    logger.critical('На этом всё')


if __name__ == '__main__':
    log_all()
