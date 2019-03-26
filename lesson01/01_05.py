__author__ = 'Шишкин Анатолий Васильевич'

'''
5. Пользователь вводит две буквы. 
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
'''

import string

alphabet = list(string.ascii_lowercase)

first_simbol = input('Введите первую латинскую букву:\n').lower()
second_simbol = input('Введите вторую латинскую букву:\n').lower()

print(f'Порядковый номер буквы "{first_simbol}" в английском алфавите - {alphabet.index(first_simbol) + 1}.\n'
      f'Порядковый номер буквы "{second_simbol}" в английском алфавите - {alphabet.index(second_simbol) + 1}.\n'
      f'Между этими буквами находится ещё букв - {alphabet.index(second_simbol) - alphabet.index(first_simbol) - 1}'
      f', а если быть точнее, то это следующие буквы '
      f'{alphabet[alphabet.index(first_simbol) + 1 : alphabet.index(second_simbol)]}.')


