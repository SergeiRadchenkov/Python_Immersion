'''
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''
class Rectangle:
    def __init__(self, side_a, side_b=None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    def perimetr(self):
        return 2 * (self.side_a + self.side_b)

    def square(self):
        return self.side_a * self.side_b


rect_1 = Rectangle(2, 4)
print(rect_1.perimetr())
print(rect_1.square())
