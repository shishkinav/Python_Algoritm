'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и
C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
[‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
__author__ = 'Шишкин Анатолий Васильевич'


def number_x16_in_x10(lst):
    return int(''.join(lst), 16)


def number_x10_in_x16(number):
    return list(hex(number)[2:])


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def main():
    lst_number_1 = [_ for _ in input('Введите первое шестнадцатеричное число:\n')]
    lst_number_2 = [_ for _ in input('Введите второе шестнадцатеричное число:\n')]
    try:
        print('Сумма введенных чисел:', end='')
        result = add(
            number_x16_in_x10(lst_number_1),
            number_x16_in_x10(lst_number_2)
        )
        print(''.join(number_x10_in_x16(result)))
        print('Произведение введенных чисел:', end='')
        result = mult(
            number_x16_in_x10(lst_number_1),
            number_x16_in_x10(lst_number_2)
        )
        print(''.join(number_x10_in_x16(result)))
    except:
        print('Что-то пошло не так!')


if __name__ == '__main__':
    main()

