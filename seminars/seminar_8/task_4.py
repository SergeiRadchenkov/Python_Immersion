'''
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
'''
import csv
import json


def export_csv_to_json(csv_file: str, json_file: str):
    final_dict = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, items in enumerate(data):
        data[i] = data[i].strip().split('|')
        data[i][1] = data[i][1].zfill(10)
        final_dict[hash(data[i][0] + data[i][1])] = data[i]
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(final_dict, file, indent=4, ensure_ascii=False)



export_csv_to_json('user_db.csv', 'new_user_db.json')