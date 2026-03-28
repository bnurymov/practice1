# Python For Loops

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Range
for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)

# Break and continue
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

# Nested loop
for x in range(3):
    for y in range(3):
        print(x, y)
