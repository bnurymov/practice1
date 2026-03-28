# Python Modules
# Import and use modules

import math
import random
import os

print(math.pi)
print(math.sqrt(16))
print(math.floor(4.7))

print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))

print(os.getcwd())

# Import specific function
from math import pow, ceil
print(pow(2, 10))
print(ceil(4.1))

# Alias
import datetime as dt
print(dt.datetime.now())
