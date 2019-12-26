# Суммировать вводимые числа, среди которых нет нулевых.
# При вводе нуля обеспечить вывод текущего значения суммы.
# При вводе числа 99999 закончить работу.

import re
list_numbers = []

sum = 0

while True:
    print("Введите число:", ends=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружены числа")

        number = int(string)
        list_numbers.append(number)

        if number == 99999:
            break
        elif number == 0:
            print("Сумма:", sum)
            else:
                sum += number

        print("Сумма:", sum)
        
