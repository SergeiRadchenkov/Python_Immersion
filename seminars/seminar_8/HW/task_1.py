'''
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию
и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.

Каждый результат должен содержать следующую информацию:
Путь к файлу или директории: Абсолютный путь к файлу или директории.
Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.

Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий,
находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory),
которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
При этом сначала добавляются файлы, а затем директории.
Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
и затем получается размер файла (size = os.path.getsize(path)).
Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)),
и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого.
Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
'''
import os
import json

PATH_DIR = 'C:\\Users\\Nitro V15\\Desktop\\Python_Immersion\\seminars\\seminar_8'


def traverse_directory(directory):
    results = []
    dir_res = []
    dir_list = os.listdir(directory)
    for obj in dir_list:
        obj_path = os.path.join(directory, obj)
        if os.path.isdir(obj_path):
            entry_dir = {
                'Path': obj_path,
                'Type': 'Directory',
                'Size': get_folder_size(obj_path)
            }
            dir_res.append(entry_dir)
        else:
            entry_file = {
                'Path': obj_path,
                'Type': 'File',
                'Size': os.path.getsize(obj_path)
            }
        results.append(entry_file)
        for dir in dir_res:
            results.append(dir)
    return results

def get_folder_size(folder_path):
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(folder_path):
        for file in file_name:
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def save_results_to_json(results):
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def save_results_to_csv(results):
    with open('results.csv', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def save_results_to_pickle(results):
    with open('results.csv', 'wb') as f:
        json.dump(results, f)


results = traverse_directory(PATH_DIR)
save_results_to_json(results)
save_results_to_csv(results)
save_results_to_pickle(results)
