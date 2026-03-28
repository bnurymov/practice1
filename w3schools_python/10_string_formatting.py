# Python String Formatting

name = "Alice"
age = 30

# f-string (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# % operator
print("My name is %s and I am %d years old." % (name, age))

# Number formatting
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")
