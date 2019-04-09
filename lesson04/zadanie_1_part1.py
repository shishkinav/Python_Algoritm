__author__ = 'Шишкин Анатолий Васильевич'

from random import randint
import cProfile


matrix = []
def create_matrix(strok, stolb):
    for stroka in range(strok):
        matrix.append([randint(0, 10) for i in range(0, stolb)])
        matrix[stroka].extend([sum(matrix[stroka])])
    return matrix


def view_matrix(matrix):
    for s in matrix:
        print(s)

def main():
    create_matrix(4, 4)
    view_matrix()


if __name__ == '__main__':
    cProfile.run('main()')
