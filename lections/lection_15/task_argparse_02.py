import argparse

parser = argparse.ArgumentParser(prog='average',
                                 description='My first argument parser',
                                 epilog='Returns the arithmetic mean')
parser.add_argument('number', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

r'''
Примеры запуска в терминале:
python .\task_argparse_01.py --help
'''
