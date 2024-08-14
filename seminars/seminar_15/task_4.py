'''
Функция получает на вход текст вида: “1-й четверг ноября”,
“3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
'''
from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='mylog.log', encoding='utf-8', level=logging.ERROR, format='%(asctime)s - %(levelname)s '
                                                                                        '- %(msg)s')


def which_day(date: str) -> int:
    try:
        months = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
        weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
        cnt, weekday, month = date.split()
        cnt = int(cnt[0])

        weekday_ind = next((i for i in range(len(weekdays)) if weekday.startswith(weekdays[i])), None)
        if weekday_ind is None:
            raise ValueError(f'Некорректный день недели: {weekday}')

        month_ind = next((i for i in range(len(months)) if month.startswith(months[i])), None)
        if month_ind is None:
            raise ValueError(f'Некорректный день недели: {month}')

        year = datetime.now().year
        date = datetime(year=year, month=month_ind, day=1)

        weekday_count = 0
        while date.month == month_ind:
            if date.weekday() == weekday_ind:
                weekday_count += 1
                if weekday_count == cnt:
                    return date.strftime('%d.%m.%Y')
            date += timedelta(days=1)

        raise ValueError(f'Не удалось найти {cnt}-й {weekday} {month}')
    except Exception as e:
        logging.error(str(e))
        return None


print(which_day('2-й четверг августа'))
