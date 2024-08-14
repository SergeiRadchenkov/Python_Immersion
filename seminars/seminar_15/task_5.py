'''
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
'''
from datetime import datetime, timedelta
import logging
import argparse


logging.basicConfig(filename='mylog.log', encoding='utf-8', level=logging.ERROR, format='%(asctime)s - %(levelname)s '
                                                                                        '- %(msg)s')

def parse_ordinal(ordinal_str: str) -> int:
    try:
        return int(ordinal_str[0])
    except ValueError as e:
        logging.error(f'Ошибка обработки порядкового номера: {str(e)}')
        raise

def which_day(ordinal: int, weekday: str, month: str) -> str:
    try:
        months = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
        weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

        if weekday.isdigit():
            weekday_ind = int(weekday) - 1
            if not (0 <= weekday_ind < 7):
                raise ValueError(f'Некорректный день недели: {weekday}')
        else:
            weekday_ind = next((i for i in range(len(weekdays)) if weekday.startswith(weekdays[i])), None)
            if weekday_ind is None:
                raise ValueError(f'Некорректный день недели: {weekday}')

        if month.isdigit():
            month_ind = int(month)
        else:
            month_ind = next((i + 1 for i in range(len(months)) if month.startswith(months[i])), None)
            if month_ind is None:
                raise ValueError(f'Некорректный день недели: {month}')

        year = datetime.now().year
        date = datetime(year=year, month=month_ind, day=1)

        weekday_count = 0
        while date.month == month_ind:
            if date.weekday() == weekday_ind:
                weekday_count += 1
                if weekday_count == ordinal:
                    return date.strftime('%d.%m.%Y')
            date += timedelta(days=1)

        raise ValueError(f'Не удалось найти {ordinal}-й {weekday} {month}')
    except Exception as e:
        logging.error(f'Ошибка обработки: {str(e)}')
        return None


def main():
    parser = argparse.ArgumentParser(description='Получили дату по порядковому номеру и месяца.')
    parser.add_argument('ordinal', type=str, nargs='?', default='1-й',
                        help='Порядековый номер дня недели в месяце (по умолчанию 1)')
    parser.add_argument('weekday', type=str, nargs='?', default=datetime.now().weekday() + 1,
                        help='День недели (по умолчанию текущий день недели)')
    parser.add_argument('month', type=str, nargs='?', default=str(datetime.now().month),
                        help='Месяц (по умолчанию текущий месяц)')

    args = parser.parse_args()

    ordinal = parse_ordinal(args.ordinal)

    result = which_day(ordinal, args.weekday, args.month)
    if result:
        print(f'Дата: {result}')
    else:
        print('Не удалось определить дату.')


if __name__ == "__main__":
    main()


'''
Запуск из командной строки:

python task_5.py 1-й четверг августа

или

python task_5.py 1 4 8
'''