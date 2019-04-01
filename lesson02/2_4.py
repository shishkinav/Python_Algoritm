__author__ = 'Шишкин Анатолий Васильевич'
'''
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''

def func_row(n):
    if int(n) == 1:
        return 1
    elif n % 2 == 0:
        return -(func_row(n - 1) / 2)
    elif n % 2 != 0:
        return -(func_row(n - 1) / 2)


while True:
    try:
        number = input('Введите количество интересующих вас элементов (для выхода введите q):\n')
        if number.lower() == 'q':
            print('Спасибо за участие')
            break
        tmp_list = []
        for i in range(1, int(number)+1):
            tmp_list.append(func_row(i))
        print(f'''
        Ряд чисел, который Вы запросили выглядит так - {tmp_list}.
        Сумма элементов этого ряда равна {sum(tmp_list)}
        ''')
    except:
        print('Количество элементов должно быть целым числом, попробуйте ещё раз.')
