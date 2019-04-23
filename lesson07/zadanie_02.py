'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
'''

from random import (
    randint,
    choice
)


def sort_massive(massive: list) -> None:
    if len(massive) <= 1:
        return massive
    else:
        num = choice(massive)

    left_el = [l_el for l_el in massive if l_el < num]
    mid_element = [num] * massive.count(num)
    right_el = [r_el for r_el in massive if r_el > num]

    return sort_massive(left_el) +\
        mid_element + sort_massive(right_el)


def main():
    lst = [randint(0, 50) for i in range(20)]
    print(lst)
    print(sort_massive(lst))


if __name__ == '__main__':
    main()