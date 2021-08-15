from random import randint

m = int(input('Введите количество колонок и строчек: '))
a = [[randint(1, 50) for _ in range(m)] for _ in range(m)]
o = '{y:<8}'
a1 = [0] * m
print()

for k in range(m):
    for b in range(m):
        print(o.format(y=a[k][b]), end='')
        a1[b] += a[k][b]
    print()
print()

for h in a1:
    print(o.format(y=h), end='')
print()


def bubble(array):
    for i in range(len(array) - 1):
        kap = 1
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                for s in range(len(array)):
                    a[s][j], a[s][j + 1] = a[s][j + 1], a[s][j]
            kap = 0
        if kap:
            break
    for i1 in range(len(a)):
        for i in range(len(a)):
            flag = 1
            for j in range(len(a) - 1):
                if (i1 + 10) % 2:
                    if a[j][i1] > a[j + 1][i1]:
                        a[j][i1], a[j + 1][i1] = a[j + 1][i1], a[j][i1]
                    flag = 0
                else:
                    if a[j][i1] < a[j + 1][i1]:
                        a[j][i1], a[j + 1][i1] = a[j + 1][i1], a[j][i1]
                    flag = 0
        if flag:
            break


bubble(a1)

print()
print()
for k in range(m):
    for b in range(m):
        print(o.format(y=a[k][b]), end='')
    print()
print()
for h in a1:
    print(o.format(y=h), end='')
print()
