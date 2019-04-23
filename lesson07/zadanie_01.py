'''
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''

from random import randint


def sort_massiv(massiv):
    for j in range(len(massiv)):
        is_sorted = True
        for i in range(len(massiv) - 1 - j):
            if massiv[i] < massiv[i + 1]:
                is_sorted = False
                massiv[i], massiv[i + 1] = massiv[i + 1], massiv[i]
        if is_sorted:
                break
    return massiv


def main():
    o_lst = [randint(-100, 100) for i in range(20)]

    print(o_lst)
    print(sort_massiv(o_lst))


if __name__ == '__main__':
    main()