# Исходные данные считаны с файла Students1.txt в директории программы.


a=[]
y2 = 0
o = '{y:<30}'
file = open('Students1.txt', encoding='utf-8')
file2 = open('Students.txt', 'w', encoding='utf-8')

for i in file:
    i1 = i.split()
    a.append(i1)
file.close()

print('Учащиеся, средний бал которых меньше 5:')
for h in a:
    t=0
    j= h[1]+ ' ' +h[0][0].upper()+'.'
    h.pop(0)
    h.pop(0)
    for h1 in h:
        t += int(h1)
    t1 = t / len(h)
    y = o.format(y=j)
    y1 = round(t1,2)
    y2 +=y1
    file2.write(y)
    file2.write(str(y1))
    file2.write('\n')
    if y1<5:
        print(y,y1)

print(o.format(y='Средний бал всех учащихся:'),round(y2 / len(a),2))
file2.close()