
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
