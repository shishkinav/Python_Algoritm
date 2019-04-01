__author__ = 'Шишкин Анатолий Васильевич'
'''
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 
127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
'''

import string


max_stolb = 10
alphabet = string.ascii_letters + string.punctuation + string.digits
count = 0
for code_char in range(32, 127 + 1):
    if count < 10:
        print(f'{code_char} - {chr(code_char)}', end='\t\t')
        count += 1
    else:
        count = 0
        print(f'{code_char} - {chr(code_char)}', end='\n')
