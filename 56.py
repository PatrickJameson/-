# Заданы M строк символов, которые вводятся с клавиатуры.
# Напечатать все центральные буквы строк нечетной длины.

import math

M = 3

list_strings = []

for i in range(0, M):
  print("Введите строку:", end=' ')
  list_strings.append(input())
  
for string in list_strings:
  strlen = len(string)

if strlen % 2 != 0:
  print(string[math.ceil(strlen/2) - 1])
