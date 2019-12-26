# Определить сумму вводимых положительных чисел.
# Причём числа с нечётными номерами (по порядку ввода) суммировать с обратным знаком, а числа с чётными номерами перед суммированием возводить в квадрат.
# Подсчитать количество слагаемых.
# При вводе первого отрицательного числа закончить работу.

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
