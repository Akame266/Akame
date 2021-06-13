a = int(input('Укажите год: '))
c = a % 400
v = a % 100
b = a % 4
print(f'Год {a} является', end=' ')
s = 'высокосным.' if c == 0 or b == 0 and not v == 0 else 'невысокосным.'
print(s)