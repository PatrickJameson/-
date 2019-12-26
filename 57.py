# Заданы M строк символов, которые вводятся с клавиатуры.
# Каждая строка содержит слово.
# Записать каждое слово в разрядку (вставить по пробелу между буквами).

M = 3

list_strings = []

for i in range(0, M):
  print("Введите строку:", end=' ')
  list_strings.append(input())
  
for string in list_strings:
  print(' '.join(string))
