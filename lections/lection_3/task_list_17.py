import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
print()
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
print()
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
