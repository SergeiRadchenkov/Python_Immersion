'''
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку.
'''
print('\n\n'.join(['\n'.join(['\t\t'.join([f'{x:^3}x{y:^3}= {x*y:^3}'
                                          for y in range(2+i, 6+i)]) for x in range(2, 11)]) for i in [0, 4]]))

#Вариает 2

print(''.join(f'{i}*{j}={i*j}\t{i+1}*{j}={(i+1)*j}\t{i+2}*{j}={(i+2)*j}\t\t{i+3}*{j}={(i+3)*j}\n'
              for i in [2,6] for j in range(1, 11)))
