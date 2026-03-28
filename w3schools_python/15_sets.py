# Python Sets
# Sets are unordered and do not allow duplicates

s = {1, 2, 3, 4, 5}
print(s)

s.add(6)          # Add item
s.discard(3)      # Remove item safely
print(s)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)      # Union
print(a & b)      # Intersection
print(a - b)      # Difference
print(a ^ b)      # Symmetric difference

print(2 in a)     # Membership check
