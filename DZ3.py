a = int(input('Введите число: '))
b = int((a%10)*100)
c = int((a-(a%10))%100)
z = int((a-(a%100))/100)
g = int(b+c+z)
print(f'Зеркальное число будет выглядеть: {g}')