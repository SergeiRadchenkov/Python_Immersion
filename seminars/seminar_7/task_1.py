'''
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''
from random import uniform, randint
MIN_SIZE = -1000
MAX_SIZE = 1000

def write_in_file(num_of_str, file_name):
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
        f.writelines('\n'.join([f'{randint(MIN_SIZE, MAX_SIZE)} | {uniform(MIN_SIZE, MAX_SIZE)}' for i in range(num_of_str)]))


print(write_in_file(12, 'seminar_7_1'))
