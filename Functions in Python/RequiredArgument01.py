def average(a,b):
    print("The Avg of a =",a,"b =",b," = ",(a+b)/2)

Num1=int(input("Enter the Number 1 : "))
Num2=int(input("Enter the Number 2 : "))

average(Num1,Num2)

def avg(a,b=5):
    print("The Avg of a =",a,"b =",b," = ",(a+b)/2)

avg(2) # a = 2 