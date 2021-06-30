import random
p = [random.randint(0, 20) for _ in range(20)]
print(p, 'кол-во уникальных чисел в сгенерированном списке p : ', len(set(p)))