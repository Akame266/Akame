a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def rev(lis):
    a = 0
    b = -1
    n = 0  # кол-во обменов
    for i in range(len(lis) // 2):
        n += 1  # колво обменов
        lis[a], lis[b] = lis[b], lis[a]
        a += 1
        b -= 1
    return print(lis)  # ,print(n)


rev(b)
rev(a)
