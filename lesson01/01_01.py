__author__ = 'Шишкин Анатолий Васильевич'

'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

number = input('Введите трёхзначное число:\n')
sum, multiple = 0, 1

for element in list(number):
    sum += int(element)
    multiple *= int(element)

print(sum, multiple, sep='\n')
