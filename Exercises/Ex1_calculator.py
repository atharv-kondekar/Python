a=int(input("Enter the First Number : "))
b=int(input("Enter the Second Number : "))
ope=input("Enter the Operator : ")

if(ope=='+'):
    print("",a,"",ope,"",b,"  : ",a+b)
elif(ope=='-'):
    print("",a,"",ope,"",b,"  : ",a-b)
elif(ope=='/'):
    print("",a,"",ope,"",b,"  : ",a/b)
elif(ope=='*'):
    print("",a,"",ope,"",b,"  : ",a*b)
elif(ope=='%'):
    print("",a,"",ope,"",b,"  : ",a%b)
elif(ope=='**'):
    print("",a,"",ope,"",b,"  : ",a**b)
elif(ope=='//'):
    print("",a,"",ope,"",b,"  : ",a//b)
else:
    print(" !! You Entered Wrong Operator !!")