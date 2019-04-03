__author__ = 'Шишкин Анатолий Васильевич'
'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
'''
from random import randint


massive = [randint(-100, 100) for i in range(0, 20)]

elements = {
    'min_i': 0,
    'max_i': 0,
    'min_v': min(massive),
    'max_v': max(massive),
    'sum': 0
}

for i, v in enumerate(massive):
    if v == elements['max_v']:
        elements['max_i'] = i
    if v == elements['min_v']:
        elements['min_i'] = i

if elements['max_i'] < elements['min_i']:
    elements['max_i'], elements['min_i'] = elements['min_i'], elements['max_i']

for i in range(elements['min_i'] + 1, elements['max_i']):
    elements['sum'] += massive[i]

print(f'''
В полученном массиве {massive} сумма элементов между 
минимальным элементом {elements['min_v']} и максимальным элементом {elements['max_v']}
не включая их равна {elements['sum']}
''')