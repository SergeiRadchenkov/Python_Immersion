from typing import Callable


def cash(func: Callable):
    _cash_dict = {}

    def wrapper(*args):
        if args not in _cash_dict:
            _cash_dict[args] = func(*args)
        return _cash_dict[args]

    return wrapper


@cash
def factorial(n: int) -> int:
    print(f'Вычисляю факторииал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
