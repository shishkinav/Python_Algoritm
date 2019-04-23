'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой –
не больше медианы. Задачу можно решить без сортировки исходного массива. Но если
это слишком сложно, то используйте метод сортировки, который не рассматривался
на уроках
'''

from random import randint, choice
from operator import attrgetter
from sys import getsizeof
from lesson07.zadanie_01 import sort_massiv
from lesson07.zadanie_02 import sort_massive

class Number:

    def __init__(self, num) -> None:
        self.num = num

    def __repr__(self) -> str:
        return f'{self.num}'

    def sort_num(self):
        return self.num


def med_left_right(data: list):
    if len(data) <= 1:
        return (False, data, False)
    else:
        med = data[int(len(data) / 2)]

    left_med = [l_el for l_el in data if l_el < med]
    med_el = [med] * data.count(med)
    right_med = [r_el for r_el in data if r_el > med]

    return (left_med, med_el, right_med)



def main():
    # Задаем натуральное число m
    m = 15
    size = 2 * m + 1
    lst = [Number(randint(0, 50)) for i in range(size)]
    tmp_lst_1 = [el.num for el in lst]
    tmp_lst_2 = tmp_lst_1.copy()
    tmp_lst_3 = tmp_lst_1.copy()

    print('Исходный массив', lst)

    # сортировка с использованием функции из стандартной библиотеки
    print('\nРазмер занимаемой памяти:', getsizeof(sorted(lst, key=attrgetter('num'))))
    print('Сортировка через sorted по объектам класса: ', sorted(lst, key=attrgetter('num')))

    # сортировка с использованием функции задания 1
    print('\nРазмер занимаемой памяти функцией задания 1:', getsizeof(sort_massiv(tmp_lst_1)))
    print('Сортировка функцией задания 1: ', sort_massiv(tmp_lst_1))

    # сортировка с использованием функции задания 2
    print('\nРазмер занимаемой памяти функцией задания 2:', getsizeof(sort_massive(tmp_lst_2)))
    print('Сортировка функцией задания 2: ', sort_massive(tmp_lst_2))

    # деление элементов по медиане
    print('\nРазмер занимаемой памяти функцией медианного распределения:', getsizeof(med_left_right(tmp_lst_3)))
    l, m, r = med_left_right(tmp_lst_3)
    if l and r:
        print(f'Исходный массив имеет медиану: {m}\n'
              f'Элементы, которые должны быть слева от медианы: {l}\n'
              f'Элементы, которые должны быть справа от медианы: {r}')
    else:
        print('Элемент в массиве всего один', med_left_right(tmp_lst_3))


if __name__ == '__main__':
    main()
