for i in range(5):
    if i == 2:
        pass  # Does nothing, just a placeholder
    print(i)

print("---")

for i in range(5):
    if i == 2:
        continue  # Skips the rest of the loop for i=2
    print(i)

print("---")

for i in range(5):
    if i == 2:
        break  # Stops the loop when i=2
    print(i)
 