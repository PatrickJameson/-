# Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами группу из M элементов,
# начинающихся с позиции K с группой из M элементов, начинающихся с позиции P.

import random
N = int(input("Введите количество элементов массива "))
M = int(input("Количесвто элементов в группе"))
K = int(input("Позиция K"))
P = int(input("Позиция P"))
a = [random.randint(0, 100) for i in range(0, N)]
print(a)

for i in range(N):
    a[K: K + M], a[P: P + M] = a[P: P + M], a[K: K + M]
print(a)
