n = int(input('Введите натуральное число n= '))
a = 2
v = 0
while a <= n:
    a *= 2
    v += 1
print(f'Натуральное число {n}, показатель степени двойки: {v}, 2**{v}={a // 2} и не превышает значение n={n}.')