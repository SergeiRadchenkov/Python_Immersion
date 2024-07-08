def facrotial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for i, num in enumerate(facrotial(10), start=1):
    print(f'{i}! = {num}')
