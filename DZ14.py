y = int(input('Введите желаемую высоту треугольника в цифре: '))
x = y * 2
print('вот оно')
for y1 in range(y):
    print()
    for x1 in range(x):
        if y1 == y or x1 == y1+y-1 or x1 == y-y1-1 or x1 < y1+y and not x-y-y1 > x1:
            print('* ', end='')
        else:
            print('  ', end='')
print()