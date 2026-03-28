# Python Try...Except

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    x = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")

# Finally block
try:
    f = open("/tmp/test.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs")

# Raise exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-1)
except ValueError as e:
    print(e)
