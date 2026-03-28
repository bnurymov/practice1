# Python If...Else

age = 20

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary (one-line if)
result = "Even" if age % 2 == 0 else "Odd"
print(result)

# Nested if
x = 10
if x > 0:
    if x > 5:
        print("Greater than 5")
    else:
        print("Between 0 and 5")
