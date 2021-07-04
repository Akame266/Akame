a = int(input('Введите год, чтобы проверить его высокосность: '))


def is_year_leap(a):
    return a % 400 == 0 or a % 4 == 0 and not a % 100 == 0


print(is_year_leap(a))
# Требует 2 пробела пайтон.
