# Задана строка символов, в которой встречается символ «.».
# Поставить после каждого такого символа системное время ПК.

from datetime import datetime
M = 3

list_strings = []
for i in range(0, M):
  print("Введите строку:", end=' ')
  list_strings.append(input())

now = str(datetime.now())

for string in list_strings:
  print(string.replace('.', '.' + now))
