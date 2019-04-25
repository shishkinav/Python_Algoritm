import hashlib


s = hashlib.sha1(b'Secret' + b'Hello, Bob!').hexdigest()
print(hashlib.sha1(b'Secret' + bytes(s.encode('utf-8'))).hexdigest())

# Задача 1. Сравнить строки с помощью хеширования
def is_eq_str(a, b):
    '''
    Главное применение хеш-функции — это быстрое сравнение двух подстрок, то есть проверка
    целостности данных. На этом основываются все остальные алгоритмы с хешами.
    Следующая функция производит сравнение двух строк, вычисляя их хеш и сравнивая его.
    '''
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
    return ha == hb


# Задача 2. Провести поиск подстроки
def rabin_karp(s, t):
    '''
    Хеши позволяют быстро искать подстроку в строке. Для этого применяется алгоритм Рабина-Карпа.
Алгоритм решения задачи:
    Дана строка s длины n, в которой мы хотим найти все вхождения строки t длины m.
    Найдем хеш строки t (всей строки целиком).
    Найдем хеши всех префиксов строки s.
    Будем двигаться по строке s окном длины m, сравнивая подстроки s(i...i+m-1).
    '''
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            return i

    return -1


def main():
    print(rabin_karp('это я привет мир', 'привет мир'))
    print(is_eq_str('привет мир', 'привет мир'))

if __name__ == '__main__':
    main()