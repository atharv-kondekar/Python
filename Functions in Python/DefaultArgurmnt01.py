def average(a=5,b=6):
    print("The Avg : ",(a+b)/2)

average()


'''
If i pass the values from the functions then 
it ignores the default arguments 
'''
def average2(x=78,y=45):
    print("The Avg : ",(x+y)/2)

average2(7,8)


# We can also write like this 
def avg(a=5,b=7):
    print("The Avg of ",a,b,"= ",(a+b)/2)

avg(3) #it takes as the a=3
avg(b=4) #it takes the b=4 