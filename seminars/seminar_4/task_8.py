'''
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''

start = 100
s = 'letter'
apples = 25
codes = 10010110101011

def func():
    temp_dict = {}
    for item in globals():
        if not item.startswith('__'):
            if item.endswith('s') and len(item) > 1:
                temp_dict[item[:-1]] = globals()[item]
                temp_dict[item] = None
    globals().update(temp_dict)


func()
print([item for item in globals().items() if not item[0].startswith('__')])
print(apple)
print(code)
