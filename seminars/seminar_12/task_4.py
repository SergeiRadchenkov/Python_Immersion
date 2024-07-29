'''
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
'''


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        weight = self.width + other.width
        height = self.height + other.height
        return Rectangle(weight, float(height))

    def __sub__(self, other):
        weight = self.width - other.width
        height = self.height - other.height
        return Rectangle(weight, float(height))

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'

    @property
    def t_width(self):
        return self.t_width

    @t_width.setter
    def t_width(self, value):
        if value <= 0:
            raise ValueError('Так нельзя')
        self.width = value

    @property
    def t_height(self):
        return self.t_height

    @t_height.setter
    def t_height(self, value):
        if value <= 0:
            raise ValueError('Так нельзя')
        self.height = value


r1 = Rectangle(1, 2)
r1.t_width = -1
