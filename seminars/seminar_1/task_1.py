'''
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
'''

n = int(input('Введите число: '))
e = int(input('Введите число: '))
cnt = 1
res = 0

while cnt <= n:
    if cnt % 2 == 0 and cnt % e != 0:
        res += cnt
    cnt += 1
print(res)