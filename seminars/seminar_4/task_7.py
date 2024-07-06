'''
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''
import random

companies = {name: [random.randint(-10000, 10000) for _ in range(random.randint(3, 10))]
             for name in ['adibas', 'hike', 'rybok']}


print(companies)


def func(dct_comp: dict) -> bool:
    for i in dct_comp:
        dct_comp[i] = sum(dct_comp[i])
    print(dct_comp)
    return all(map(lambda x: x > 0, dct_comp.values()))


print(func(companies))

# Вариант 2
def my_func(dct_comp: dict) -> bool:
    for i in dct_comp.values():
        if sum(i) < 0:
            return False
    return True
