'''Локальные переменные'''

def func(y: int) -> int:
    x = 100
    x +=100
    print(f'In func {x = }') # Принтим для примера, а не для привычки
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')
