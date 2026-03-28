# Python Functions

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Default argument
def power(base, exp=2):
    return base ** exp

print(power(3))      # 9
print(power(3, 3))   # 27

# *args (variable number of args)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))

# **kwargs (keyword arguments)
def display(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

display(name="Bob", age=25)
