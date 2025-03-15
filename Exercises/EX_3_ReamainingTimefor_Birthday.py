import time

print("Enter Your Birth Date ")
day=int(input("Enter the Day : "))
month=int(input("Enter the Month : "))
year=int(input("Enetr the Year : "))

result=time.localtime()
age=result.tm_year-year 

if year<result.tm_year or (result.tm_mon == month and result.tm_mday < day ):
    age-=1

print("Your Current Age is : ",age)


Rm_day=result.tm_mday-day
Rm_mon=result.tm_mon-month
Rm_sec=result.tm_sec

if(Rm_day < 0 ):
   Rm_day = -(Rm_day)
if(Rm_mon < 0):
    Rm_mon = -(Rm_mon)


print("Remaining Time for your Birthday is : ")
print("Months : ",Rm_mon,"Days : ",Rm_day,"Sec : ",Rm_sec)