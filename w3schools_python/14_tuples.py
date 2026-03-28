# Python Tuples
# Tuples are immutable (cannot be changed)

coords = (10, 20, 30)
print(coords)
print(coords[0])      # Access
print(len(coords))    # Length

# Unpack tuple
x, y, z = coords
print(x, y, z)

# Tuple with one item
single = (42,)
print(type(single))

# Loop through tuple
for val in coords:
    print(val)
