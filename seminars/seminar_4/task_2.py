'''
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''


def my_func(x):
    result = []
    for i in set(x):
        result.append(ord(i))
    result.sort(reverse=True)
    return result


_str = input('Введите строку: ')
print(my_func(_str))

# Вариант 2
print([ord(i) for i in sorted(list(set(_str)))[::-1]])
