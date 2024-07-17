'''
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
'''
import csv
import json
import os

PATH_DB = 'user_db.json'
CSV_FILE = 'user_db.csv'


def loas_json():
    if os.path.exists(PATH_DB):
        with open('user_db.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def input_name():
    return input('Введите имя: ')

def input_id(dict_users: dict):
    list_id = set()
    for users in dict_users.values():
        for user in users:
            for u_id in user:
                list_id.add(u_id)

    while True:
        u_id = input('Введите ID: ')
        if u_id not in list_id and u_id.isdigit():
            return u_id
        print('Такой ID занят, введите заново')


def input_lvl():
    while True:
        lvl = input('Введите уровень доступа: ')
        if lvl.isdigit() and 0 < int(lvl) < 8:
            return lvl


def create_users():
    while True:
        user_db = loas_json()
        name = input_name()
        if not name:
            break
        u_id = input_id(user_db)
        lvl = input_lvl()

        if lvl in user_db:
            user_db[lvl].append({u_id: name})
        else:
            user_db[lvl] = [{u_id: name}]
        with (
            open(PATH_DB, 'w', encoding='utf-8') as file_json,
            open(CSV_FILE, 'w', encoding='utf-8') as file_csv
        ):
            json.dump(user_db, file_json, indent=4, ensure_ascii=False)
            result = []
            for lvl, users in user_db.items():
                for user in users:
                    for u_id, name in user.items():
                        result.append([name, u_id, lvl])
            csv_writer = csv.writer(file_csv, dialect='excel', delimiter='|', lineterminator='\n')
            csv_writer.writerows(result)




create_users()

