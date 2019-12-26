# Заданы M строк символов, которые вводятся с клавиатуры.
# Каждая строка представляет собой последовательность символов, включающих в себя вопросительные знаки.
# Заменить в каждой строке все имеющиеся вопросительные знаки звёздочками.

import re

M = 3

list_strings = []
for i in range(0, M):
  print("Введите строку:", end=' ')
  list_strings.append(input())
  
for string in list_strings:
  string = re.sub(r'\?', '*', string)
  print(string)
