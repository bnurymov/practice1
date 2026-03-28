# Python Lists

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])         # Access item
print(fruits[-1])        # Last item
print(fruits[0:2])       # Slicing

fruits.append("mango")   # Add item
fruits.remove("banana")  # Remove item
fruits.insert(1, "kiwi") # Insert at position
print(fruits)

print(len(fruits))       # Length
print("apple" in fruits) # Check membership

# Loop through list
for fruit in fruits:
    print(fruit)
