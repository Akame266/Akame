a1 = int(input('Введите начальную координату по оси x: '))
b1 = int(input('Введите начальную координату по оси y: '))
a2 = int(input('Введите конечную координату по оси x: '))
b2 = int(input('Введите конечную координату по оси y: '))
x = abs(a2 - a1)
y = abs(b2 - b1)
if x == 2 and y == 1 or y == 2 and x == 1:
    print('Ход конем может быть совершен на данную клетку.')
else:
    print('Конь не может сделать ход на данную клетку.')