import numpy as np

print("The ramdom values between the 10 and 50 is : ",np.random.randint(10,50))

arr1D=np.random.randint(10,50,4)
print("\n The Random 4 values between the 10 and 50 is : ",arr1D)

print("\n The Conversion of the : ",arr1D,"\n into 2D is : \n",arr1D.reshape(2,2))