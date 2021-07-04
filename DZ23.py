a = int(input())


def season(a):
    return 'Winter' if a in (1, 2, 12) else 'Spring' if a in (3, 4, 5) else 'Summer' if a in (6, 7, 8) else 'Autumn' if\
a in (9, 10, 11) else 'Введите цифру месяца корректно'


print(season(a))
