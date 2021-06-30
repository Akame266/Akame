# s = 'Сегодня очень жарко.\nВчера тоже было жарко.\nНо сегодня несравненно жарко.'
# Можете использовать это пример сверху, Вместо строк 3-7 -
# первую или ввести строки самостоятельно с запятыми или точками ^_^
s = ''
for n in range(3):
    n = str(input(''))
    s += n + ' '
s = s.strip()
# print(s)
s = s.lower()
s = s.replace('.', '')
s = s.split()
y = tuple(s)
# print(y)
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
h = sorted(d.items(), key=lambda x: x[0], reverse=True)  # Нашел функцию для красоты на выводе (если потребуется)
# print(h)
print('Максимально часто встречается в тексте слово:', d[k1])