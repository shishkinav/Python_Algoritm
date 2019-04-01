__author__ = 'Шишкин Анатолий Васильевич'
'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран 
это число и сумму его цифр.
'''


def check_number(number):
    '''
    :param number: string
    :return: (number, sum_char_in_number)
    '''
    try:
        s = 0
        for _ in number:
            s += int(_)
        return s
    except:
        return False


numbers = input('Введите через пробел натуральные числа, которые вы хотите '
                'сравнить:\n').split()
# numbers = '77 11 77 12 56 49 16 59 71'.split()
numbers_dict = {_: check_number(_) for _ in numbers}

max_key = sorted(numbers_dict)[-1:][0]
max_value = numbers_dict[max_key]
print(max_key, max_value)
tmp_key_list = []
for key, value in numbers_dict.items():
    if value > max_value:
        tmp_key_list.append(key)
if len(tmp_key_list) > 0:
    max_key = tmp_key_list[-1:][0]

print(f'''
Вы ввели числа {numbers}
Наибольшее по сумме цифр в нём - это {max_key} и сумма цифр равна - {numbers_dict[max_key]}
Вот словарь значений для проверки:
{numbers_dict}
''')
