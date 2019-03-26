__author__ = 'Шишкин Анатолий Васильевич'

'''
Доп
2. Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать. 
После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число. 
В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).
'''
import random

number = random.randint(1, 100)
game = True
count = 1
MAX_COUNT = 10

while game:
    choice = int(input('Введите число от 1 до 100:\n'))
    if choice == number:
        print('Вы победили! Это действительно было число', choice)
        game = False
    elif choice < number:
        print('Искать надо выше')
    elif choice > number:
        print('Искать надо ниже')
    count += 1
    if count > MAX_COUNT:
        print(f'Вы проиграли, Вами использовано {count - 1} из {MAX_COUNT} попыток.')
        game = False
