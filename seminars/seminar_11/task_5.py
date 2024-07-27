'''
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
'''


class Rectagle:
    '''Класс прямоугольник'''
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return self.a + self.b

    def __add__(self, other):
        '''Сложение сторон прямоугольника и создание нового объекта'''
        if isinstance(other, Rectagle):
            return Rectagle(self.a + other.a, self.b + other.b)
        raise TypeError

    def __sub__(self, other):
        '''Вычетание сторон прямоугольника'''
        if self.a > other.a and self.b > other.b:
            return Rectagle(self.a - other.a, self.b - other.b)

    def __str__(self):
        return f'Прямоугольник со сторонами ({self.a}, {self.b})'


rect_1 = Rectagle(7, 15)
rect_2 = Rectagle(6, 14)
print(rect_1 - rect_2)
print(rect_1 + rect_2)
