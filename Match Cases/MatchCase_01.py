x = int(input("Enter the Number : "))

match x:
    case 2:
        print("Number is 2")
    
    case 10:
        print("Number is 10 ")
    
    case _ :
        print("Default Case Run")