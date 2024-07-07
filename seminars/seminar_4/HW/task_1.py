'''
Напишите функцию для транспонирования матрицы transposed_matrix,
принимает в аргументы matrix, и возвращает транспонированную матрицу.
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


# transposed_matrix = transpose(matrix)
def transpose(lst: list):
    new_list = []
    for i in range(len(lst[0])):
        new_row = []
        for j in range(len(lst)):
            new_row.append(matrix[j][i])
        new_list.append(new_row)
    return new_list

transposed_matrix = transpose(matrix)
print(transposed_matrix)

# Вариант 2
def transpose(matrix):
    # определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # создаем новую матрицу с размерами, поменянными местами
    transposed = [[0 for row in range(rows)] for col in range(cols)]

    # заполняем новую матрицу значениями из старой матрицы
    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]

    return transposed
