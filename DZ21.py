a = int(input('Введите длину стороны квадрата: '))  # Можно закоментить и сразу юзать вписывая длинну.


def square(a):
    b = 4 * a
    d = 2 * a ^ 2
    c = (d ^ 2) // 2
    return b, d, c


print('Периметр, диагональ и площадь квадрата соответственно равны:', square(a))