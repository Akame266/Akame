y = int(input('Введите желаемую высоту треугольника в цифре: '))
x = int(y)
print('вот оно')
for y1 in range(y):
    print()
    for x1 in range(x):
        if x1+x//2 == y1 or x1+x//2 == y-y1-1 or x1 == y1+y//2 or x-x1+x//2 == y1+1 or y1 <= y // 2 and not \
        x-x//2-x1 > y1 and not y1+y//2 < x1:
            print('* ', end='')
        else:
            print('  ', end='')
print()