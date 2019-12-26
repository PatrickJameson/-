# Заданы M строк, которые вводятся с клавиатуры.
# Подсчитать количество пробелов в каждой из строк.

import re

M = 3

list_strings = []
for i in range(0, M):
  print("Введите строку:", end=' ')
  list_strings.append(input())
  
for string in list_strings:
  count_spaces = len(re.findall(r'\s', string))
  print("В строке \"%s\" %s пробелов" % (string, count_spaces)) 
