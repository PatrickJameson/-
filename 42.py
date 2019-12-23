# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, образуют ли элементы массива, расположенные перед первым отрицательным элементом, убывающую последовательность.

def check_array(array):
  if array[0]<0:
     return False

for i in range (1,len(array)):
  if array[i]< 0:
   return True
 if array [i-1]> array[i]:
    return False
array =[2,1,0,-1,3,4,-2,4]
print (check_array(array))
