__author__ = 'Шишкин Анатолий Васильевич'

import cProfile
from functools import wraps


def memorize(func):
    @wraps(func)
    def f(n, memory=[0, 1]):
        '''
        без декоратора время исполнения при n = 30 составляет 1,45
        с декоратором memorize время исполнения при n = 490 составляет 0,004, при значении выше выдаёт ошибку рекурсии
        оптимизировав алгоритм с рекурсивного на итерируемый, удалось запусть программу на n > 500, для сравнения:
            время исполнения при n = 10000 составляет 0,005, т.е. прирост производительности ещё примерно в 20 раз
        '''
        if n < 2:
            return n
        pp = 0
        p = 1
        for i in range(n - 1):
            pp, p = p, pp + p
        return p
    return f


@memorize
def decorated_f(n):
    return decorated_f(n - 1) + decorated_f(n - 2)


def main():
    decorated_f(10000)


if __name__ == '__main__':
    cProfile.run('main()')
