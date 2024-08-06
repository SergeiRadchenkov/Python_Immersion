'''
Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.
Исходный код в редакторе кода надо доработать, чтобы вызывалось исключение NegativeValueError.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины.
Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2).
Убедимся, что r1.width корректно установлен на 5,
а создание r4 вызывает исключение NegativeValueError с текстом Ширина должна быть положительной, а не {value}

test_height: Тестирование инициализации ширины и высоты.
Созданы прямоугольники r2 с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4.
При необходимости выбрасывать исклчение NegativeValueError с текстом Высота должна быть положительной, а не {value}

test_perimeter: Тестирование вычисления периметра.
Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter() возвращает 20.
Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади.
Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() возвращает 25.
Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения.
Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
Выполняем операцию сложения r1 + r2 и проверяем,
что полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания.
Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
Выполняем операцию вычитания r1 - r2 и проверяем,
что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).
'''
import doctest


class NegativeValueError(Exception):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width < 0:
            return f'Ширина должна быть положительной, а не {self.width}'
        elif self.height < 0:
            return f'Высота должна быть положительной, а не {self.height}'


class Rectangle:

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height
        if self.width < 0 or self.height < 0:
            raise NegativeValueError(self.width, self.height)

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


def test_width():
    """
    >>> r1 = Rectangle(5)
    >>> r1.width
    5
    >>> r4 = Rectangle(-4)
    NegativeValueError: Ширина должна быть положительной, а не -4
    """


def test_height():
    """
    >>> r2 = Rectangle(3, 4)
    >>> r2.width
    3
    >>> r2.height
    4
    """


def test_perimeter():
    """
    >>> r1 = Rectangle(5)
    >>> r1.perimeter()
    20
    >>> r2 = Rectangle(3, 4)
    >>> r2.perimeter()
    14
    """

def test_area():
    """
    >>> r1 = Rectangle(5)
    >>> r1.area()
    25
    >>> r2 = Rectangle(3, 4)
    >>> r2.area()
    12
    """

def test_addition():
    """
    >>> r1 = Rectangle(5)
    >>> r2 = Rectangle(3, 4)
    >>> r3 = r1 + r2
    >>> r3.width
    8
    >>> r3.height
    6.0
    """

def test_subtraction():
    """
    >>> r1 = Rectangle(5)
    >>> r2 = Rectangle(3, 4)
    >>> r3 = r1 - r2
    >>> r3.width
    2
    >>> r3.height
    2.0
    """


import sys

# Открываем файл для записи
with open('pytest_output.txt', 'w') as file:
    # Перенаправляем stdout в файл
    sys.stdout = file

    # Запускаем pytest.main() с нужными параметрами
    __file__ = None

    doctest.testmod(extraglobs={'__file__': __file__})

# Возвращаем stdout в исходное состояние
sys.stdout = sys.__stdout__
# Считываем содержимое файла
with open('pytest_output.txt', 'r') as file:
    lines = file.readlines()
    # first_line = file.readline()
    # first_five_lines = lines[:1]

import re

file_name = "pytest_output.txt.txt"

# Открываем файл на чтение
with open('pytest_output.txt', "r") as file:
    # Считываем содержимое файла
    file_content = file.read()

# Используем регулярное выражение для удаления "line" и чисел после него
cleaned_content = re.sub(r'File "__main__", line \d+', '', file_content)

# Записываем обновленное содержимое обратно в файл
with open(file_name, "w") as file:
    file.write(cleaned_content)

with open(file_name, 'r') as new_file:
    file_contents = new_file.read()
    # Выводим содержимое файла на экран
    print(file_contents)
