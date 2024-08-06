class ValidateRectangle:
    def __init__(self, min_value: int = 1):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError('Invalid type of input')
        if value < self.min_value:
            raise ValueError('Invalid value of input')


class Rectangle:
    width = ValidateRectangle()
    height = ValidateRectangle()

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'



if __name__ == '__main__':
    r1 = Rectangle(1, 2)
    print(r1)
    r1.width = 5
    print(r1)
