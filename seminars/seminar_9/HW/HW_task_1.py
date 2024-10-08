'''
Создайте функцию generate_csv_file(file_name, rows),
которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл.
Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json.
Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json
будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
'''
import random as rnd
import csv
import json


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        for _ in range(rows):
            row_num = [rnd.randint(1, 11) for _ in range(3)]
            csv_writer.writerow(row_num)


def save_to_json(func):
    def wrapper(file_name):
        results = []
        with open(file_name, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                a = int(row[0])
                b = int(row[1])
                c = int(row[2])
                roots = func(a, b, c)
                result = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'roots': roots
                }
                results.append(result)
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
    return wrapper


@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    if d == 0:
        return -b / (2 * a)
    if d > 0:
        return (((-b - d ** 0.5) / (2 * a)), (-b + d ** 0.5) / (2 * a))


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)


# Вариант 2
import csv
import json
import random

def save_to_json(func):
    def wrapper(*args):
        result_list = []
        with open(args[0], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data = {'parameters': [a, b, c], 'result': result}
                result_list.append(data)
        with open('results.json', 'w') as f:
            json.dump(result_list, f)
    return wrapper

@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

