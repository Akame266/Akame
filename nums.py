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

numrev(1000,16)

print(bin(35))
print(hex(1000))