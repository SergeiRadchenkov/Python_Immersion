'''
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него функцию rename_files
'''

code_to_write = '''
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=(1, 100)):
    dir_list = os.listdir('test_folder')
    count = 10**num_digits
    for obj in dir_list:
        if os.path.isfile(f'test_folder/{obj}') and obj.endswith(f'.{source_ext}'):
            new_name = f'{desired_name}{str(count+1)[-num_digits:]}.{target_ext}'
            os.rename(f'test_folder/{obj}', f'test_folder/{new_name}')
            count +=1
    files = [file for file in os.listdir('test_folder')]
    print(', '.join(files))
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)

