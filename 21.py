# Определить значение функции Z = 1/(XY ) при произвольных X и Y .
import random
A = 1
B = 100
C = int(random.randint(A, B))
D = int(random.randint(A, B))
F = 1 / (C*D)
print("Функция равна ",F)
