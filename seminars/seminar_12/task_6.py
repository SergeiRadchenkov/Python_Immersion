'''
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
'''


class Value:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        setattr(instance, self.param_name, self._validate(value))

    def _validate(self, value: int):
        if not (self.min_value < value < self.max_value):
            raise ValueError
        return value

class Rectangle:
    widht = Value(10, 100)
    height = Value(10, 100)

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @property
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


a = Rectangle(11, 12)
print(a.area)
