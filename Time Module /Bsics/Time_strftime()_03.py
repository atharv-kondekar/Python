import time

result=int(time.strftime("%H",time.localtime()))

if(7<=result<12):
    print("Good Morning Sir :) ")
elif(12<=result<16):
    print("Good Afternoon sir :)")
elif(16<=result<19):
    print("Good Evening sir :)")
elif(19<=result<23):
    print("Good Night Sir :)")
else:
    print(" Sir is Sleeping...... ")