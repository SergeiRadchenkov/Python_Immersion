'''
� Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки
'''
from task_4_directory import my_game
from task_4_directory import puzzles

if __name__ == '__main__':
    for puzzle_str, answers in puzzles():
        my_game(puzzle_str, answers, 3)
