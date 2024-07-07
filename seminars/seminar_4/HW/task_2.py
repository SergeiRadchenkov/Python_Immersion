'''
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''


def key_params(**kwargs):
    new_dict = {}

    for key, value in kwargs.items():
        if value is None or isinstance(value, (str, int, float)):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key

    return new_dict


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)

