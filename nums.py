from string import ascii_uppercase
print(ascii_uppercase)
def numrev(x,y=2):
    a=[]
    b = ''
    while x > 0:
        a1 = x%y
        a.append(a1)
        x = x//y
        print(a)
    a.reverse()
    for o in a:
        b += str(o)
    return print(a,b)


print(hex(1000))
print(hex(966))
print(hex(999))
print(hex(1))
print(hex(28))
