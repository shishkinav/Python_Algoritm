__author__ = 'Шишкин Анатолий Васильевич'

import cProfile


def f(n):
    '''
    без декоратора время исполнения при n = 30 составляет 1,45
    '''
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)


def main():
    print(f(30), end=' ')


if __name__ == '__main__':
    cProfile.run('main()')
