a = input('Введите строку: ')
v, c = a.find('h'), a.rfind('h')
print(a[:v+1] + a[v+1:c].replace('h', 'H') + a[c:])