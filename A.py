'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''
def BinInsCheck(l, v):
    b = 0
    e = len(l)
    while True:
        m = b + (e - b) // 2
        if e == b:
            l.insert(e, v)
            return False
        if v == l[m]:
            return True

        if v > l[m]:
            b = m + 1
        if v < l[m]:
            e = m

def Repeated(s):
    l = list(map(int, s.split()))
    s = []

    for v in l:
        if BinInsCheck(s, v):
            return v
    return None

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')
fi.readline()
print(Repeated(fi.readline()), file=fo)
