# Можно ли в квадратном зале площадью S поместить круглую сцену радиусом R так,
# чтобы от стены до сцены был проход не менее K?
import math
S = int(input("Укажите площадь зала "))
R = int(input("Укажите радиус сцены "))
K = int(input("Укажите необходимую ширину прохода "))
A = math.sqrt(S)
print (A, " Длинна стены")
if (A - 2*R >= K):
    print("Размер сцены соответствует условию")
else:
    print("Размер сцены не соответствует условию")
