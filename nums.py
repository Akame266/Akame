def numrev(x, y=2):
    from string import ascii_uppercase
    a2 = ascii_uppercase.lower()
    a = []
    s = '0123456789' + a2
    b = ''
    while y > 36:
        y = int(input('Введите желаемую систему исчисления не более 36: '))
    while x > 0:
        a1 = x % y
        if a1 < y:
            a.append(s[a1])
        else:
            a.append(a1)
        x = x // y
    a.reverse()
    d = {
        2: 'b',
        8: 'o',
        16: 'x'
    }
    if y in d.keys():
        b1 = '0' + str(d.get(y))
    else:
        j1 = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
        y = str(y)
        b1 = '0' + y.translate(j1)
    for o in a:
        b += str(o)
    b2 = b1 + b
    return print(b2)


numrev(333, 16)
print(hex(333))
print()
numrev(894, 8)
print(oct(894))
print()
numrev(111, 2)
print(bin(111))
print()
numrev(222, 8)
print(oct(222))
print()
print(hex(879))
numrev(879, 16)
print()
numrev(678, 36)
print()
numrev(12312, 55)
