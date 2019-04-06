__author__ = 'Шишкин Анатолий Васильевич'
'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

from random import randint


matrix = []
for stroka in range(4):
    matrix.append([randint(0, 10) for i in range(0, 5)])
for s in matrix:
    print(s)

for i in range(len(matrix[0])):
    min_v = matrix[0][i]
    for j in range(len(matrix)):
        if matrix[j][i] < min_v:
            min_v = matrix[j][i]
    if i == 0:
        max_v = min_v
    else:
        if min_v > max_v:
            max_v = min_v

print(f'''
Максимальный элемент среди минимальных по столбцам равен {max_v}''')

# max_v = 0
# tmp_list = []
# for i in range(len(matrix[0])):
#     min_v = matrix[0][i]
#     for j in range(len(matrix)):
#         if matrix[j][i] < min_v:
#             min_v = matrix[j][i]
#     tmp_list.append(min_v)
#
# print(f'''
# Максимальный элемент среди минимальных по столбцам равен {max(tmp_list)}''')

