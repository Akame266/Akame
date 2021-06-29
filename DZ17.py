s = 'Я иду туда, куда, не знаю, но иду, почему, не знаю, но иду, когда прийду, когда не знаю, тогда прийду.'
s1 = s.replace(',', '')
s1 = s1.replace('.', '')
s1 = s1.lower()
s2 = tuple(s1.split())
k = 0
f = []
while True:
    n = s2[k]
    w = s2.count(str(n))
    k += 1
    r = (n, w)
    f.append(r)
    if k == len(s2):
        break
d1 = dict(f)
print('Слова и их кол-во повторений в строке:', d1)


