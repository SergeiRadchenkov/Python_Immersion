'''
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
'''
# Не доделана

from task_4 import*


class Logger:
    db = {}

    def __init__(self, path):
        self.__class__.db = load_json(path)
        self.level = None

    def authorize(self, the_id, name):
        user = User(name, the_id)
        if user in self.__class__.db:
            self.level = self.__class__.db[the_id]['level']
            return self.level
        else:
            raise Exception('Пользователь с такими данными не найден')


if __name__ == '__main__':
    PATH = 'my_json.json'
    logger = Logger(PATH)
    print(f'Уровень доступа: {logger.authorize(77, 'Вацок')}')
