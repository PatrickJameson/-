# Даны двещественные числа X и Y . Вычислить Z. Z = √(X x Y) при X > Y, Z = ln(X + Y ) в противном случае.
import math
X = float(input("Введите вещественное число X "))
Y = float(input("Введите вещественное число Y "))
if X > Y:
    Z = math.sqrt(X * Y)
    print(Z," =")
else:
    Z = math.log(X + Y, math.e)
    print(Z," =")
