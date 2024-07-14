'''
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
    Функция принимает следующие параметры:
    ✔ расширение
    ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    ✔ количество файлов, по умолчанию 42
    ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''
import os
import string
from random import randbytes, sample, randint


def create_files(extension, min_len=6, max_len=30, min_bytes=256,  max_bytes=4096, num_of_files=42, my_path='muss'):
    for i in range(num_of_files):
        name = ''.join(sample(string.ascii_lowercase + string.ascii_lowercase, randint(min_len, max_len)))
        if not os.path.isdir(my_path):
            os.mkdir(my_path)
        with open(f'{my_path}/{name}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_bytes, max_bytes)))

if __name__ == '__main__':
    create_files(extension='txt', num_of_files=3, )
