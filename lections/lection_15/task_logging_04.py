import logging
from other import log_all


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Использум вызов функции из другого модуля')
log_all()
