import time

start=time.perf_counter()
time.sleep(5)
end=time.perf_counter()

print("Execution Time = ",end-start)