__author__ = 'Шишкин Анатолий Васильевич'
'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
'''
from random import randint


massive = [randint(-100, 100) for i in range(0, 20)]

max_negativ = -100
max_negativ_index = 0

for i in massive:
    if i < 0 and i > max_negativ:
        max_negativ = i
        max_negativ_index = massive.index(i)

print(f'В полученном массиве {massive} максимальным отрицательным элементом является:\n'
      f'{max_negativ} и его позиция (индекс) {max_negativ_index}')

