from random import randint

MAX_COUNT = 5


def get_data():
    '''Получение данных из внешнего источника.'''
    if result := randint(0, 3):
        return result
    else:
        raise ConnectionError


count = 0
while count < MAX_COUNT:
    count +=1
    try:
        data = get_data()
        break
    except ConnectionError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')

print(data)  # noqa
