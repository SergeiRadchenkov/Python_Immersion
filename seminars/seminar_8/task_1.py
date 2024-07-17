'''
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''
import json
from pathlib import Path


def get_input(p: Path) -> 'File':
    with open(p) as f:
        return f.readlines()


def parse_input(c: list[str]) -> list[tuple[str, str]]:
    out = []
    for line in c:
        tmp = line.strip().split('->')
        try:
            out.append((tmp[0].title(), tmp[1]))
        except:
            pass
    return out


def jasonize(c: list[tuple[str, str]]):
    print()
    with open('t1_out.json', 'w') as f_o:
        json.dump(c, f_o, indent=2)
    pass


if __name__ == '__main__':
    a = get_input(Path('../seminar_7/result.txt'))
    a = parse_input(a)
    jasonize(a)
