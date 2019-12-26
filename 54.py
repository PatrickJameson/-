# Заданы M строк слов, которые вводятся с клавиатуры (в каждой строке – одно слово).
# Вводится слог (последовательность букв). Подсчитать количество таких слогов в каждой строке.

import re

M = 2

list_strings = []
for i in range(0, M):
  print("Введите в строку:", end=' ')
  list_strings.append(input())

print("Введите слог :", end=' ')
syllable = input()

for string in list_strings:
  count = len(re.findall(syllable, string))
  print("В строке \"%s\"слог \"%s\"встречается %s раз " % (string, syllable, count))
