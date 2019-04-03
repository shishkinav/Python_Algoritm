__author__ = 'Шишкин Анатолий Васильевич'
'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
from random import randint


min_index, max_index = 0, 0

massive = [randint(0, 100) for i in range(0, 20)]
# massive = [21, 79, 84, 6, 35, 56, 43, 96, 95, 54, 20, 12, 34, 83, 47, 53, 57, 86, 24, 16]

element_dict = {
    'min_value': sorted(massive)[:1][0],
    'max_value': sorted(massive)[-1:][0],
}

print(massive)
for i, v in enumerate(massive):
    if v == element_dict['min_value']:
        massive[i] = element_dict['max_value']
    elif v == element_dict['max_value']:
        massive[i] = element_dict['min_value']

print(massive)