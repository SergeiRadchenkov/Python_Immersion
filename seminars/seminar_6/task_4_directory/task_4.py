from task_4_directory.task_5_dict_puzzle import puzzles

def my_game(pazzl_str: str, answer: list, cnt: int):
    count = cnt
    print(pazzl_str)
    while cnt > 0:
        us_answer = input(f'У вас {cnt} попыток. Введите ваш ответ: ')
        if us_answer not in answer:
            cnt -= 1
            if cnt == 0:
                print(f'У вас осталось {cnt} попыток. Вы не угадали!')
                return
            print('Ответ не верный')
        else:
            print(f'Вы угадали загадку за {count - cnt + 1} попыток')
            return

if __name__ == '__main__':
    for puzzle_str, answers in puzzles():
        my_game(puzzle_str, answers, 3)
