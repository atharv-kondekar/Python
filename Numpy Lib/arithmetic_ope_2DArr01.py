import numpy as np

list1=[1,2,3,4,5]
list2=[5,4,3,2,1]
list3=[1,2,5,4,3]

arr1=np.array([list1,list2,list3])
print("The Arr1 : \n",arr1)


arr2=np.array([list3,list1,list2])
print("\n The Arr2 : \n",arr2)


print("\n The Arr1*Arr2 : \n",arr1*arr2)

print("\n The Arr1 + Arr2 : \n",arr1+arr2)

print("\n The Arr1-Arr2 : \n",arr1-arr2)

print("\n The Arr1 / Arr2 : \n",arr1/arr2)

print("\n The Arr1 == Arr2  : \n",arr1==arr2)

print("\n The Arr1[arr1<3]  : \n ",arr1[arr1<3])