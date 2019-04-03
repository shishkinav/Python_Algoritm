__author__ = 'Шишкин Анатолий Васильевич'
'''
4. Определить, какое число в массиве встречается чаще всего.
'''

from random import randint


massive = [randint(0, 100) for i in range(0, 20)]

count_char = {}

for element in massive:
    if str(element) not in count_char.keys():
        count_char[str(element)] = 1
    else:
        count_char[str(element)] += 1

max_key, max_value = sorted(count_char.items(), key=lambda x: x[1], reverse=True)[0]

print(f'Чаще всего в массиве {massive} встречается число {max_key}, оно встречается {max_value} раз(а).')