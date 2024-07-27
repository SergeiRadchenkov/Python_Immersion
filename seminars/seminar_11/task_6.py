'''
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''
from functools import total_ordering

@total_ordering
class Rectangle:
    '''Класс прямоугольник'''
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a + self.b

    def __add__(self, other):
        '''Сложение сторон прямоугольника и создание нового объекта'''
        if isinstance(other, Rectangle):
            return Rectangle(self.a + other.a, self.b + other.b)
        raise TypeError

    def __sub__(self, other):
        '''Вычетание сторон прямоугольника'''
        if self.a > other.a and self.b > other.b:
            return Rectangle(self.a - other.a, self.b - other.b)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами ({self.a}, {self.b})'


rect_1 = Rectangle(7, 15)
rect_2 = Rectangle(6, 14)
print(rect_1 - rect_2)
print(rect_1 + rect_2)
print(rect_1 < rect_2)
print(rect_1 == rect_2)
print(rect_1 > rect_2)
print(rect_1 != rect_2)
print(rect_1 >= rect_2)
print(rect_1 <= rect_2)
