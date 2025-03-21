import numpy as np


list1=[1,2,3,4,5]
list2=[5,4,3,2,1]
list3=[1,2,5,4,3]

arr1=np.array([list1,list2,list3])

print("\n The original array : \n",arr1)

print("\n The Arr1 transpose : \n",arr1.reshape(5,3))