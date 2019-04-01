import os
import re


def create_file(name_file, path, data):
    with open(os.path.join(path, name_file), 'a', encoding='utf-8') as file:
        global AUTHOR
        file.write(AUTHOR)
        file.write(f"'''\n{data}\n'''")


AUTHOR = "__author__ = 'Шишкин Анатолий Васильевич'\n"

if __name__ == '__main__':
    PATH = os.getcwd()
    pattern = "([0-9]+)\.\s+\w+"

    if 'DZ_for_lesson_02' in os.listdir(PATH):
        with open('DZ_for_lesson_02', encoding='utf-8') as file:
            data = file.read().split('\n')
    else:
        print('Файл для чтения отсутствует в каталоге запущенного скрипта')

    for line in data:
        if line:
            numberLine = re.findall(pattern, line[:5])
            if f'2_{numberLine[0]}.py' in os.listdir(PATH):
                print(f'Файл 2_{numberLine[0]}.py существует, удаление приведет к потере кода!')
            else:
                create_file(f'2_{numberLine[0]}.py', PATH, line)
                print(f'Файл 2_{numberLine[0]}.py создан')
