__author__ = 'Шишкин Анатолий Васильевич'

'''
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

import string

alphabet = list(string.ascii_lowercase)

number = int(input('Введите номер буквы в английском алфавите:\n'))
print(f'Вы ввели номер следующей буквы - "{alphabet[number - 1]}"')


