import time

start = time.monotonic()
time.sleep(2)
end = time.monotonic()
print("Elapsed time:", end - start, "seconds")
