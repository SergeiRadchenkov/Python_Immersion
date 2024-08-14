'''
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
'''
import os
import logging
import argparse
from collections import namedtuple


logging.basicConfig(filename='file_info.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(msg)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])


def gather_directory_info(directory: str):

    for root, dirs, files in os.walk(directory):

        for name in files:
            file_path = os.path.join(root, name)
            parent_dir = os.path.basename(os.path.dirname(file_path))
            name, extension = os.path.splitext(name)
            info = FileInfo(name=name, extension=extension, is_dir=False, parent_dir=parent_dir)
            logging.info(f"Обработан файл: {info}")

        for name in dirs:
            dir_path = os.path.join(root, name)
            parent_dir = os.path.basename(os.path.dirname(dir_path))
            info = FileInfo(name=name, extension='', is_dir=True, parent_dir=parent_dir)
            logging.info(f"Обработан каталог: {info}")


def main():
    parser = argparse.ArgumentParser(description='Сбор информации о содержимом директории')
    parser.add_argument('directory', type=str, help='Путь к директории')

    args = parser.parse_args()

    gather_directory_info(args.directory)


if __name__ == '__main__':
    main()


'''
Пример использования:

python task_6.py "C:\\Users\\Nitro V15\\Documents"

'''