def facrotial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


for i, num in enumerate(facrotial(10), start=1):
    print(f'{i}! = {num}')
