# Нарисуйте полную блок-схему алгоритма сортировки массива «методом пузырька».

import random
n = 25
a = [random.randint(0, 100) for i in range(n)]
print(a)
N = 1
while N < n - 1:
    for i in range(n - N):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    N += 1


print(a)
