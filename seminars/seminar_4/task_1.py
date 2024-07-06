'''
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки
'''

data = 'Вот так и хочется писать и писать'


def my_func(data: str):
    data_splitted = data.lower().split()
    max_len = len(max(data_splitted, key=len)) + 1
    data_splitted.sort()
    for i, item in enumerate(data_splitted, 1):
        print(f'{i}.{item:>{max_len}}')


my_func(data)
