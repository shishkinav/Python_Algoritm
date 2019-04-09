'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Выписать подряд все целые числа от двух до n (2, 3, 4, …, n).
Пусть переменная p изначально равна двум — первому простому числу.
Зачеркнуть в списке числа от 2p до n считая шагами по p (это будут числа кратные p: 2p, 3p, 4p, …).
Найти первое незачёркнутое число в списке, большее чем p, и присвоить значению переменной p это число.
Повторять шаги 3 и 4, пока возможно.

2  3     5     7           11    13          17    19          23                29
'''

import cProfile

#
# def create_list_Eratosfen(n):
#     lst = [False, False] + [True for i in range(n - 2)]
#     tmp_l = []
#     for i in range(2, n + 1):
#         if lst[i]:
#             tmp_l.append(i)
#             for number in range(i + 1, n + 1):
#                 if number % i == 0:
#                     if lst[number]:
#                         lst.insert(number, False)
#     print(tmp_l)
#     return lst
#
#
# def main():
#     n = 50
#     tmp_lst = create_list_Eratosfen(n)
    # for el in enumerate(tmp_lst):
    #     if el[0] > n:
    #         break
    #     else:
    #         if el[1]:
    #             print(el)

def create_list_Eratosfen(n):
    lst = {i: True for i in range(2, n + 1)}
    # tmp_l = []
    for i in range(2, n + 1):
        if lst[i]:
            for number in range(i + 1, n + 1):
                if number % i == 0:
                    if lst[number]:
                        lst[number] = False
    return lst


def main(number=1, n=10):
    tmp_lst = create_list_Eratosfen(n)
    print([x for x in tmp_lst.items() if x[1]][number - 1][0])


if __name__ == '__main__':
    cProfile.run(f'main({5}, {10000})')