import time

"""
%Y = Is For the Year 
%d = for the Day
%m = << Small m >> for the Month

Now Make Capital 

%M = <<Capital M >> for the minute
%H = for the Hour
%S = for the Seconds

%A = Name of the Day in week 
%B = name of the MOnths in the Year 
"""

print("The Year : ",time.strftime("%y",time.localtime()))
print("The Month : ",time.strftime("%m",time.localtime()))
print("The Day of the Month : ",time.strftime("%d",time.localtime()))
print("The Hour of the Day : ",time.strftime("%H",time.localtime()))
print("The minute of the hour : ",time.strftime("%M",time.localtime()))
print("The Secnd of the Minute : ",time.strftime("%S",time.localtime()))
print("The Name of the Day in the Week : ",time.strftime("%A",time.localtime()))
print("The Name of the Month : ",time.strftime("%B",time.localtime()))
