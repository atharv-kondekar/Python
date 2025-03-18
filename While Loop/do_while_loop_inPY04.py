num=float(input("Enter the number that you want the factotial of it : "))
i=1
fact=1

while True:
    fact=fact*i
    i=i+1

    if(i>num):
        break

print("The factorial of the ",num," is : ",fact)