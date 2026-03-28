# Python While Loops

i = 0
while i < 5:
    print(i)
    i += 1

# Break
i = 0
while True:
    if i == 3:
        break
    print(i)
    i += 1

# Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# While with else
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished")
