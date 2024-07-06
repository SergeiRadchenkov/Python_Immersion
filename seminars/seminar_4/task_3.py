'''
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
'''


def my_func(x):
    lst = x.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])

    lst.sort()
    dct = {chr(i):i for i in range(lst[0], lst[1] + 1)}
    return dct

_str = input('Введите два числа: ')
print(my_func(_str))

# Вариант 2
def dict_unicode(some_str: str) -> dict:
    # lims = list(map(int, some_str.split()))
    lims = sorted([int(i) for i in some_str.split()])
    return {chr(i): i for i in range(lims[0], lims[1] + 1)}


print(dict_unicode(_str))
