import time

start=time.process_time()

for _ in range(10000000):
    pass

end=time.process_time()

print("The CPU time Program used  : ",end-start)