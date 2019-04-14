'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
__author__ = 'Шишкин Анатолий Васильевич'
import re


def average_profit(dict_companies):
    shared_profit = 0
    for k, v in dict_companies.items():
        shared_profit += sum(v)
    average_profit = shared_profit / (len(dict_companies) * 4)
    return average_profit


def print_graduate_companies(dict_companies):
    print('Предприятия, в которых прибыль за год ниже среднего:')
    for k, v in dict_companies.items():
        if average_profit(dict_companies) > sum(v) / len(v):
            print(k)
    print('Предприятия, в которых прибыль за год выше среднего:')
    for k, v in dict_companies.items():
        if average_profit(dict_companies) < sum(v) / len(v):
            print(k)


def main():
    companies = {}
    while True:
        try:
            n = int(input('Введите количество предприятий:\n'))
            break
        except:
            print('Количество предприятий должно быть целым числом, попробуйте ещё раз.')
    for i in range(n):
        name_company = input('Введите наименование предприятия:\n')
        while True:
            try:
                profit = [float(x) for x in re.sub(',', '.', input(f'Введите через пробел прибыль предприятия '
                                                                           f'{name_company} по 4 кварталам:\n')).split()]
                if len(profit) == 4:
                    break
            except:
                print('Четыре вводимых значения через пробел должны быть цифрами, попробуйте ещё раз.')
        companies[name_company] = profit

    print_graduate_companies(companies)


if __name__ == '__main__':
    main()
