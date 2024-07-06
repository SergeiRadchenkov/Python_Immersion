'''
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''

def my_sort(some_lst: list):
    for i in range(1, len(some_lst)):
        for j in range(len(some_lst)-i):
            if some_lst[j] > some_lst[j + 1]:
                some_lst[j], some_lst[j + 1] = some_lst[j + 1], some_lst[j]


lst = [2, 4, 8, 1, 3, 9, 5]
print(lst)
my_sort(lst)
print(lst)
