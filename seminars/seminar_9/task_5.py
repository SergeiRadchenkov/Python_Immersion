'''
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
'''
from task_3 import decor as json_decor
from task_2 import decor as param_control_decor
from task_4 import outer as counter


@counter(3)
@json_decor
@param_control_decor
def guess_number(a: int, b: int):
    print(f'У тебя {b} попыток угадать число!')
    while b:
        guess = int(input('Введи число: '))
        if guess > a:
            print(f'Загаданное число меньше, чем {guess}')
        elif guess < a:
            print(f'Загаданное число больше, чем {guess}')
        else:
            print(f'Ты угадал! Было загадано {a}')
            return f'Угадал за {b} попыток! Было загадано {a}.'
        b -= 1
    print('У тебя закончились попытки')
    return f'Не угадал! Было загадано {a}.'


guess_number(321, 2 )
