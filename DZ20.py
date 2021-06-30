import random
p = [random.randint(0, 20) for _ in range(20)]
n = [random.randint(10, 30) for _ in range(20)]
print('Первый и второй списки: ', p, n)
# ЭТО ВАРИАНТ С КОЛ-ВОМ УНИКАЛЬНЫХ ЗНАЧЕНИЙ В ДВУХ СПИСКАХ ОДНОВРЕМЕННО
# i = set(p + n)
# print(i)
r = len(set(p + n))
print('Кол-во уникальных чисел в 2 списках одновременно, вместе?', r)


# НЕ СОВСЕМ ПОНЯЛ СУТЬ ЗАДАНИЕ ПОЭТОМУ ВЫЛОЖИЛ СУММУ УНИКАЛЬНЫХ КАК В ПЕРВОМ И ВО ВТОРОМ ПО ОТДЕЛЬНОСТИ
# import random
# p = [random.randint(0, 20) for _ in range(20)]
# n = [random.randint(10, 30) for _ in range(20)]
# print(p, n)
# s1 = len(set(p))
# s2 = len(set(n))
# s = s1 + s2
# print(s1, s2, s)
