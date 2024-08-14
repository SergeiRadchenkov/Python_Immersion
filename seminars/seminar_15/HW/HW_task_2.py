'''
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
'''
from datetime import datetime
import logging
import argparse

logging.basicConfig(filename='mystr.log', filemode='a', encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MyStr(str):
    def __new__(cls, value: str, author: str):
        if not isinstance(value, str) or not isinstance(author, str):
            logging.error(f"Ошибка: Неверные типы аргументов: value={type(value)}, author={type(author)}")
            raise TypeError("value и author должны быть строками")
        instance = super().__new__(cls)
        instance.value = value
        instance.author = author
        instance.time = datetime.now()

        logging.info(f'Создан MyStr: "{instance.value}" (Автор: {instance.author}, Время: {instance.time})')
        return instance

    def __str__(self):
        formatted_time = self.time.strftime('%Y-%m-%d %H:%M')
        return f'{self.value} (Автор: {self.author}, Время создания: {formatted_time})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


def main():
    parser = argparse.ArgumentParser(description="Создание объекта MyStr")
    parser.add_argument("value", type=str, help="Текстовое значение строки")
    parser.add_argument("author", type=str, help="Автор строки")

    args = parser.parse_args()

    try:
        my_str = MyStr(args.value, args.author)
        print(my_str)
    except Exception as e:
        logging.error(f"Ошибка при создании MyStr: {e}")
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()


'''
Примеры запуска в консоле:

python HW_task_2.py "Пример текста" "Иван"
python HW_task_2.py "Я делаю свою домашку" "Сергей"
python HW_task_2.py "Я хорошо постарался" "Сергей"
'''