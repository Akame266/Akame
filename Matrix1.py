from random import randint
m = int(input('Введите количество колонок: '))  # колонки
n = int(input('Введите количество строк: '))  # строки
a = [[randint(0, 100) for _ in range(m)] for _ in range(n)]
a1 = [0] * m
o = '{y:<8}'
print()
for k in range(n):
    s = 0
    for b in range(m):
        s += a[k][b]
        print(o.format(y=a[k][b]), end='')
        a1[b] += a[k][b]
    print ('\t',s)
print()
for h in a1:
    print(o.format(y=h),end='')


# Если без доп переменной o, которая для формата, в условии в атачче запрещенно более 1 переменной
# for k in range(n):
#     s = 0
#     for b in range(m):
#         s += a[k][b]
#         print(a[k][b], end='\t\t')
#         a1[b] += a[k][b]
#     print ('\t',s)
# print()
# for h in a1:
#     print(h,end='\t\t')