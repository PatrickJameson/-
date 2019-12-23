# Дан одномерный массив числовых значений, насчитывающий N элементов. 
# Дано положительное число T.
# Разделить это число между положительными элементами массива пропорционально значениям этих элементов и добавить полученные доли к соответствующим элементам.

def create_array(array,t):
 res=[]
 for element in array:
  if element>0:
   res.append(element+element/t)
  else:
   res.append(element)
 return res
array=[2,1,0,-1,3,4,-2,4]
print (create_array(array,15.0))
