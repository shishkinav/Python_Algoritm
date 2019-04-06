__author__ = 'Шишкин Анатолий Васильевич'
'''
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна 
вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
В конце следует вывести полученную матрицу.
'''
from random import randint

# вариант автоматического заполнения матрицы значениями и суммами в конце каждой строки
matrix = []
for stroka in range(4):
    matrix.append([randint(0, 10) for i in range(0, 4)])
    matrix[stroka].extend([sum(matrix[stroka])])

for s in matrix:
    print(s)

# вариант с ручным вводом по четыре числа
matrix = []
for stroka in range(4):
    matrix.append([int(i) for i in input(f'Введите 4 числа через пробел для строки {stroka + 1}:\n').split()])
    matrix[stroka].extend([sum(matrix[stroka])])

for s in matrix:
    print(s)