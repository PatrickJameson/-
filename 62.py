# Даны число P и число H. Определить сумму чисел меньше P, произведение чисел больше H и количество чисел в диапазоне значений P и H.
# При вводе числа равного P или H, закончить работу.

import re

list_numbers = []

sum = 0
sum_count = 0

i = 1
while True:
  print("Введите число:", end=' ')
  string = re.sub(r'[^0-9\-]+', '', input())
  if len(string) == 0:
    print("В строке не обнаружено число")
    continue
    
  number = int(string)
  list_numbers.append(number)

  if i % 2 != 0:
    number *= -1
  
  else:
    number *= number
  
  sum += number
  i += 1
  if list_numbers[len(list_numbers) - 1] < 0:
    break
  
print("Сумма:", sum)
print("Количество слагаемых:", i)
