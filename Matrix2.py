from random import randint

m = int(input('Введите количество колонок и строчек: '))
a = [[randint(1, 50) for _ in range(m)] for _ in range(m)]
o = '{y:<8}'
a1 = [0] * m
print(a)
print()

for k in range(m):
    for b in range(m):
        print(o.format(y=a[k][b]), end='')
        a1[b] += a[k][b]
    print()
print()


def bubble(array):
    for i in range(len(array) - 1):
        flag = 1
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                for s in range(len(array)):
                    a[s][j], a[s][j + 1] = a[s][j + 1], a[s][j]
            flag = 0
        if flag:
            for q in range(len(array)-1):
                for q1 in range(len(array) - 1 - q):
                    for s in range(len(array)):
                        a[s][j], a[s][j + 1] = a[s][j + 1], a[s][j]

            break


for h in a1:
    print(o.format(y=h), end='')
print()

bubble(a1)
print()
print(a)
print()
for k in range(m):
    for b in range(m):
        print(o.format(y=a[k][b]), end='')
    print()
print()
for h in a1:
    print(o.format(y=h), end='')
print()