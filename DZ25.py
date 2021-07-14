d = {
   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']
}

k = []
u = {}
l = []
for i, i1 in d.items():
    h = tuple(i1),i
    k.append(h)
f = dict(k)
u = dict(l)
for t,t1 in f.items():
    for e in t:
        if e in u.keys():
            u[e].append(t1)
        else:
            h2 = [t1]
            h1 = e,h2
            l.append(h1)
            u = dict(l)
print('Перевернутый словарь будет выглядеть следующим образом:',u)

