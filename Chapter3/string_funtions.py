#      STRING MANIPULATION 

s="hello"
print(s.upper())      #op = HELLO 
print(s.capitalize()) #op =Hello

a="HELLO"
print(s.lower())      #op =hello

c=" hello world "
print(c.title())      #op =" Hello World "
print(c.strip())      #op ="hello world"
print(c.lstrip())     #op ="hello world "
print(c.rstrip())     #op =" hello world"



#        STRING SEARCHING 
#Note :- String Searching Funtions Are Case Sensative 

b="Hello World"
print(b.find("World"))   #op = 6(starting index of "World")
print(b.find("world"))   #op = -1 ( case sensative )

print(b.index("World"))    #op = 6(starting index of "World")
# print(b.index("world"))  #op = generates ERROR

print(b.startswith("Hello")) #op = True
print(b.startswith("hello")) #op = False

print(b.endswith("World"))  #op = True
print(b.endswith("world"))  #op = False 



#           STRING REPLACEMENT AND SPLITTING 
s="Hello World"
print(s.replace("World","Python"))   #Op = Hello Python 

d="apple,banana,grape"
print(d.split(","))     #op = ['apple', 'banana', 'grape']
print(d.split(":"))     #op = ['apple,banana,grape']
e="apple:banana:grape"
print(e.split(":"))     #op = ['apple', 'banana', 'grape']

f=["Hello" , "World"]
print("".join(f))        #op = HelloWorld
print(" ".join(f))       #op = Hello World


#        STRING FORMATING 

name=input("\n Enter the Name : ")
age=int(input("\n Enter the Age : "))
print("\n My Name is : {} & my age is :{}".format(name,age))  #op = My Name is : leo & my age is :3

print(f"\n My Name is {name} & my age is :{age}")             #op = My Name is : leo & my age is :3



#          STRING CHECKING 

g="23UAM061"
print(g.isalnum())        #op= TRUE
print(g.isalpha())        #op= False
print(g.isdigit())        #op= False
print(g.isspace(),"\n")   #op= False


h="ABCSFSA"
print(h.isalpha())        #op= TRUE

i="1234456"
print(i.isdigit())        #op= TRUE

j=" "
print(j.isspace())        #op= TRUE

