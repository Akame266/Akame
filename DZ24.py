a = int(input('Введите переменную a: '))
b = int(input('Введите переменную b: '))
c = input('Введите операцию: ')


def arithmetic(a, b, c):
    dict_operation = {
        '+': a + b,
        '-': a - b,
        '/': a / b,
        '*': a * b
    }
    return dict_operation.get(c, 'Неизвестная операция')


print('Значение выражения:', arithmetic(a, b, c))
