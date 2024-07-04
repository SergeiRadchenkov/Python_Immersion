'''
Дан список повторяющихся элементов lst.
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
'''
lst = [1, 1, 2, 2, 3, 3]

duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)

