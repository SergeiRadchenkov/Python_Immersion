'''
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
'''
data = [1, 4.5, 'string', 1, 4.5, True, True, 'string']

for i in range(len(data)):
    print(f'Порядковый номер: {i + 1}')
    print(f'Значение: {data[i]}')
    print(f'Адрес в памяти: {id(data[i])}')
    print(f'Размер: {data[i].__sizeof__()}')
    print(f'Хэш: {hash(data[i])}')
    if isinstance(data[i], int | float):
        print('Это число')
    if isinstance(data[i], str):
        print('Это строка')
    print('\n' + '='*30 + '\n')
