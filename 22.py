# Даны вещественные числа: A, B, C. Определить, выполняются ли неравенства A < B B > C
# и какое именно неравенство выполняется.
import sys
A = float(input("Введите вещественное число A "))
B = float(input("Введите вещественное число B "))
C = float(input("Введите вещественное число C "))
if A < B and B > C:
    print("Оба неравенства выполняются")
    sys.exit(0)
if A < B:
    print("Выполняется неравенство А < B")
if B > C:
    print("Выполняется неравенство B > C")
