'''
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

file_path = "C:/Users/User/Documents/example.txt"

def get_file_info(path_file):
    a = b = c = ''
    plus_str = ''
    for i in path_file:
        plus_str += i
        if i == '/':
            a += plus_str
            plus_str = ''
        if i == '.':
            b += plus_str
            plus_str = ''
        c = '.' + plus_str
    d = a, b[:-1], c
    return d


print(get_file_info(file_path))


# Вариант 2
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

print(get_file_info(file_path))