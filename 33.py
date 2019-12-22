# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Выполнить перемещение элементов массива по кругу вправо, т. е. A[1] → A[2]; A[2] → A[3]; ... A[n] → A[1].

import random
N = int(input("Введите количество элементов массива "))
a = [random.randint(0, 100) for i in range(0,N)]
print(a)
if (len(a) % 2 == 1):
    end = N
else:
    end = N-1


for i in range(end-1):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)
