def Factorial(Number):
    if(Number == 0):
        print("Factorial is 1 ")
    
    else:
        fact=1
        for i in range(1 , Number + 1):
            fact=fact*i
        print("Factotial of the ",Number," is : ",fact)
    
Num=int(input("Enter the Number : "))
Factorial(Num)