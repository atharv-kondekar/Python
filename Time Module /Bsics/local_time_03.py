import time
result=time.localtime()
print(result)

# We Can also access like this 

print(result.tm_year)
print(result.tm_mon)
print(result.tm_mday)
print(result.tm_hour)
print(result.tm_min)
print(result.tm_sec)
print(result.tm_wday)
print(result.tm_yday)
print(result.tm_isdst)