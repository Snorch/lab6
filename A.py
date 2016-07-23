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
def Repeated(s):
    l = list(map(int, s.split()))
    for v in l:
        if l.count(v) == 2:
            return v
    return -1

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')
fi.readline()
print(Repeated(fi.readline()), file=fo)
