x=int(input("Enter Number : "))

match x:
    case 0:
        print("X is Zero")
    
    case 1:
        print("First Case  Executed")
    
    case 5:
        print("5th Case Executed")

    case _ if x==50:           #First Ddefault Case 
        print(x,"is  50")
    
    case _ if x==90:           #Second Default Case 
        print(x,"is  Equal to 90")
    
    case _ :                   #Final Default Case 
        print("The Default Case Executed ")
        print("The X is : ",x)