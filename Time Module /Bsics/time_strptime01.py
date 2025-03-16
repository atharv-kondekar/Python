import time

current="16 march 2025"
"""
string = 16 march 2025 
Format = %d %B    %Y
"""
result=time.strptime(current,"%d %B %Y")
print(result)


time_str="16 4 2025"
"""
string = 16 4 2025 
Format = %d %m %Y
"""
ans=time.strptime(time_str,"%d %m %Y")
print(ans)