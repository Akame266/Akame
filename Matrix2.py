from random import randint

m = int(input('Введите количество колонок и строчек: '))
a = [[randint(1, 50) for _ in range(m)] for _ in range(m)]


def bubble(array):
    o = '{y:<8}'
    a1 = [0] * len(array)
    for k in range(len(array)):
        for b in range(len(array)):
            print(o.format(y=array[k][b]), end='')
            a1[b] += a[k][b]
        print()
    print()

    for h in a1:
        print(o.format(y=h), end='')
    print()
    for i in range(len(a1) - 1):
        kap = 1
        for j in range(len(a1) - 1 - i):
            if a1[j] > a1[j + 1]:
                a1[j], a1[j + 1] = a1[j + 1], a1[j]
                for s in range(len(array)):
                    array[s][j], array[s][j + 1] = array[s][j + 1], array[s][j]
            kap = 0
        if kap:
            break
    for i1 in range(len(array)):
        for i in range(len(array)):
            flag = 1
            for j in range(len(array) - 1):
                if (i1 + 10) % 2:
                    if array[j][i1] > array[j + 1][i1]:
                        array[j][i1], array[j + 1][i1] = array[j + 1][i1], array[j][i1]
                    flag = 0
                else:
                    if array[j][i1] < array[j + 1][i1]:
                        array[j][i1], array[j + 1][i1] = array[j + 1][i1], array[j][i1]
                    flag = 0
        if flag:
            break
    print()
    print()
    for k in range(len(array)):
        for b in range(len(array)):
            print(o.format(y=array[k][b]), end='')
        print()
    print()
    for h in a1:
        print(o.format(y=h), end='')
    print()


bubble(a)
