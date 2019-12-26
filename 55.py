# Заданы M строк слов, которые вводятся с клавиатуры (в каждой строке – одно слово).
# Вводится слог (последовательность букв). Удалить данный слог из каждой строки.

import re

M = 3

list_strings = []

for i in range(0, M):
  print("Введите в строку:", end=' ')
  list_strings.append(input())
  
print("Введите слог:", end=' ')
syllable = input()

for string in list_strings:
  string = re.sub(syllable, '', string)
  print(string)
