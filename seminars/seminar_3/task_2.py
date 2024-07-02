'''
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа
'''
from pprint import pp

a = (1, 2, 3, '1', '2', '3', True, False, None, [1])
out = dict()

for i in a:
    if type(i) not in out:
        out[type(i)] = []
        out[type(i)].append(i)
pp(out)

print()
# Вариант 2
a = (1, 2, 3, '1', '2', '3', True, False, None, [1])
out = dict()
for i in a:
    out.setdefault(type(i),[])
    out[type(i)].append(i)

pp(out)

print()
# Вариант 3
tlp = (1, 'String', [1, 2], [2, 3, 4], 'String2', {'one': 1})
result = {}

for item in tlp:
    if type(item) in result:
        result[type(item)].append(item)
    else:
        result[type(item)] = [item]

print(result)