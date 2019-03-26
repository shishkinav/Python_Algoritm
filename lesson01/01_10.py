__author__ = 'Шишкин Анатолий Васильевич'

'''
Доп
1. Дан файл  с логинами и паролями. Найдите топ10 самых популярных паролей.
'''
import re
from collections import Counter, OrderedDict

pattern = '\w+;(.+)\n'
pwd_list = []

with open('pwd.txt') as file:
    text = file.read()
    pwd_list = re.findall(pattern, text)
pwd_set = Counter(pwd_list)


pwd_set_sorted_by_value = OrderedDict(sorted(pwd_set.items(), key=lambda x: x[1], reverse=True))
top10 = 1
print('Список ТОП10 используемых паролей:')
for pwd, count in pwd_set_sorted_by_value.items():
    print(f'{top10} номинант: вид пароля {pwd}, из выборки повторяется {count} раз.')
    top10 += 1
    if top10 > 10:
        break