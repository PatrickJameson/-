# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Из элементов исходного массива построить два новых.
# В первый должны входить только элементы с положительными значениями, а во второй — только элементы с отрицательными значениями.

def create_2array(array):
 positive= []
 negative= []
 for element in array:
  if element <0:
   negative.append(element)
  if element >0:
   positive.append(element)
 return positive,negative
array = [2,1,0,-1,3,4,-2,4]

print (create_2array(array))
