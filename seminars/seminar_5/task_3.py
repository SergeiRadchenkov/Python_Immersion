'''
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
'''
my_txt = 'Строка любителей однострочников'
my_dict = {elem: ord(elem) for elem in my_txt}
iter_dict = iter(my_dict.items())
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))

