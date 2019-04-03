import os, re


def create_file(name_file, path, data):
    with open(os.path.join(path, name_file), 'a', encoding='utf-8') as file:
        global AUTHOR
        file.write(AUTHOR)
        file.write(f"'''\n{data}\n'''")


AUTHOR = "__author__ = 'Шишкин Анатолий Васильевич'\n"
name_file_with_DZ = 'DZ_for_lesson_03'
number_lesson = name_file_with_DZ.split('_')[3]

if __name__ == '__main__':
    PATH = os.getcwd()
    pattern = "([0-9]+)\.\s+\w+"

    if name_file_with_DZ in os.listdir(PATH):
        with open(name_file_with_DZ, encoding='utf-8') as file:
            data = file.read().split('\n')
    else:
        print('Файл для чтения отсутствует в каталоге запущенного скрипта')

    for line in data:
        if line:
            numberLine = re.findall(pattern, line[:5])
            if f'2_{numberLine[0]}.py' in os.listdir(PATH):
                print(f'Файл {number_lesson}_{numberLine[0]}.py существует, удаление приведет к потере кода!')
            else:
                create_file(f'{number_lesson}_{numberLine[0]}.py', PATH, line)
                print(f'Файл {number_lesson}_{numberLine[0]}.py создан')
