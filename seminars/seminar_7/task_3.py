'''
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
'''

def open_files(file_name1, file_name2):
    names = numbers = None
    with (
        open(file_name1, 'r', encoding='utf-8') as f1,
        open(file_name2, 'r', encoding='utf-8') as f2
    ):
        names = f1.readlines()
        numbers = f2.readlines()

    numbers = list(map(lambda x: int(x.strip().split(' | ')[0]) * float(x.strip().split(' | ')[1]), numbers))
    names = list(map(lambda x: x.strip(), names))
    print(f'{numbers = }\n{names = }')
    list_to_write = list(zip(names, numbers))
    print(f'{list_to_write = }')

    with open('result.txt', 'a', encoding='utf-8') as f:
        for st in list_to_write:
            if st[1] > 0:
                f.write(f'{st[0].upper()} -> {round(st[1])}\n')
            else:
                f.write(f'{st[0].lower()} -> {abs(st[1])}\n')


open_files('file_names.txt',  'seminar_7_1.txt')
