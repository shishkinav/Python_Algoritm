__author__ = 'Шишкин Анатолий Васильевич'

import cProfile


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def f(n):
    '''
    без декоратора время исполнения при n = 30 составляет 1,45
    с декоратором memorize время исполнения при n = 490 составляет 0,004, при значении выше выдаёт ошибку рекурсии
    '''
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)


def main():
    print(f(490), end=' ')


if __name__ == '__main__':
    cProfile.run('main()')
