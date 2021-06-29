s = 'Сегодня очень жарко.\nВчера тоже было жарко.\nНо сегодня несравненно жарко.'
print(s)
s = s.lower()
s = s.replace('.', '')
s = s.split()
y = tuple(s)
print(y)
l = []
n = 0
k1 = 0
while True:
    n1 = y.count(y[n])
    k = (n1,y[n])
    l.append(k)
    n += 1
    if k1 < n1:
        k1 = n1
    if n == len(y):
        break
d = dict(l)
dict(sorted(d.items()))
print(d)
print('Максимально часто встречается в тексте слово:', d[k1])