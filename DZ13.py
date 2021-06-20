y = int(input('Введите желаемую высоту треугольника в цифре: '))
y += 1
x = y * 2 -1
print('вот оно')
for y1 in range(y):
    print()
    for x1 in range(x):
        if y1 == y-1 or x1 == y1+y-1 or x1 == y-y1-1:
            print('* ', end='')
        else:
            print('  ', end='')