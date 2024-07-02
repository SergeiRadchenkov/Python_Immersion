'''
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
'''
import decimal
from decimal import Decimal
import math

decimal.getcontext().prec = 42
d = Decimal(float(input('Введите диаметр: ')))
c = Decimal(math.pi) * pow((d / 2), 2)
s = Decimal(math.pi) * d

print(f'S = {s}, C = {c}')