from string import ascii_uppercase

a2 = ascii_uppercase.lower()
print(a2)


def numrev(x, y=2):
    a = []
    b = ''
    if y == 2:
        while x > 0:
            a1 = x % y
            a.append(a1)
            x = x // y
        a.reverse()
        b1 = '0' + str(a2[-3])
    for o in a:
        b += str(o)
    b2 = b1 + b
    return print(b2)


numrev(226)
