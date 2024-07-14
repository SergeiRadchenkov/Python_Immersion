'''
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
a. принимать параметр желаемое конечное имя файлов desired_name.
При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере num_digits.
c. принимать параметр расширение исходного файла source_ext .
Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла target_ext.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории.
'''
import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
for i in range(10):

    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()


def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    if name_range:
        desired_name = desired_name[name_range[0]-1:name_range[1]]
        print(desired_name)
    dir_list = os.listdir('test_folder')
    count = 10**num_digits
    for obj in dir_list:
        if os.path.isfile(f'test_folder/{obj}') and obj.endswith(f'.{source_ext}'):
            new_name = f'{desired_name}{str(count+1)[-num_digits:]}.{target_ext}'
            os.rename(f'test_folder/{obj}', f'test_folder/{new_name}')
            count +=1
    files = [file for file in os.listdir('test_folder')]
    print(', '.join(files))


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

# Вариант 2
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    # Получаем список файлов в текущей директории
    files = os.listdir('test_folder')

    # Фильтруем только нужные файлы с указанным расширением
    filtered_files = [file for file in files if file.endswith(source_ext)]

    # Сортируем файлы по имени
    filtered_files.sort()

    # Задаем начальный номер для порядкового номера
    num = 1

    # Переименовываем файлы
    for file in filtered_files:
        # Получаем имя файла без расширения
        name = os.path.splitext(file)[0]

        # Если задан диапазон, обрезаем имя файла
        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        # Переименовываем файл
        path_old = os.path.join(os.getcwd(), folder_name, file)
        path_new = os.path.join(os.getcwd(), folder_name, new_name)
        os.rename(path_old, path_new)

        # Увеличиваем порядковый номер
        num += 1

