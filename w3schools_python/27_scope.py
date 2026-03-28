# Python Scope (LEGB rule)

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("inner:", x)    # local

    inner()
    print("outer:", x)        # enclosing

outer()
print("global:", x)           # global

# global keyword
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print("counter:", counter)    # 2
