__author__ = 'Шишкин Анатолий Васильевич'

import cProfile, timeit
from lesson04.zadanie_1_part1 import (
    create_matrix,
    view_matrix
)


def search_max_with_min_var1(matrix):
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


def search_max_with_min_var2(matrix):
    tmp_list = []
    for i in range(len(matrix[0])):
        min_v = matrix[0][i]
        for j in range(len(matrix)):
            if matrix[j][i] < min_v:
                min_v = matrix[j][i]
        tmp_list.append(min_v)

    print(f'''
    Максимальный элемент среди минимальных по столбцам равен {max(tmp_list)}''')


def main():
    matrix = create_matrix(50, 50)
    view_matrix(matrix)
    search_max_with_min_var1(matrix)
    search_max_with_min_var2(matrix)


if __name__ == '__main__':
    cProfile.run('main()')