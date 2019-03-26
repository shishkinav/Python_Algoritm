__author__ = 'Шишкин Анатолий Васильевич'

'''
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

a, b, c = int(input('Введите первое число:\n')),\
          int(input('Введите второе число:\n')), \
          int(input('Введите третье число:\n'))
# b <= a <= c
if b <= a and a <= c:
    average_number = a
# a <= b <= c
elif a <= b and b <= c:
    average_number = b
# a <= c <= b
elif a <= c and c <= b:
    average_number = c
# c <= a < b
elif c <= a and a <= b:
    average_number = a
# c <= b <= a
elif c <= b and b <= a:
    average_number = b
print('Среднее число равно -', average_number)