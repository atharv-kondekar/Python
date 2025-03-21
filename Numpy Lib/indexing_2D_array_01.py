import numpy as np

list1=[1,2,3,4,5]
list2=[5,4,3,2,1]
list3=[1,2,5,4,3]

arr=np.array([list1,list2,list3])
''' 
        columns 
       0 1 2 3 4 
Rows     
  0  | 1 2 3 4 5 |
  1  | 5 4 3 2 1 |
  2  | 1 2 5 4 3 |

'''


# Indexing The array 
print("\n The Arr[:,1] : ",arr[:,1])

print("\n The Arr[1:,1:3] : \n",arr[1:,1:3])

print("\n The Arr[1:,3:] : \n",arr[1:,3:])

print("\n The Arr[:,2:4] : \n",arr[:,2:4])

print("\n The Arr[:,[0,4]]: \n",arr[:,[0,4]])

print("\n The Arr[[0,2],:] : \n ",arr[[0,2],:])

print("\n The Array[:,:] : \n",arr[:,:])
