a = input('Введите строку: ')
b = input('Введите искомый символ: ')
s = a.find(b)
if s == -1:
    print('искомый символ не найден.')
else:
    print(s, end=' ')
while s != -1:
    r = s + 1
    s = a.find(b, r)
    if s == -1:
        break
    print(s, end=' ')