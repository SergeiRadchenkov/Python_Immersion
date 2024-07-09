'''
Создайте функцию генератор чисел Фибоначчи fibonacci.
'''

def fibonacci():
    fib = 0
    pre_fib = 1
    while(True):
        yield fib
        temp = fib + pre_fib
        fib = pre_fib
        pre_fib = temp


f = fibonacci()
for i in range(10):
    print(next(f))

# Вариант 2
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

