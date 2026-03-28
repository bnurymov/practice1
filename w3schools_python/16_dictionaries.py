# Python Dictionaries
# Key-value pairs

person = {
    "name": "Alice",
    "age": 30,
    "city": "Almaty"
}

print(person["name"])       # Access
print(person.get("age"))    # Safe access

person["email"] = "alice@example.com"  # Add item
person["age"] = 31                     # Update item
del person["city"]                     # Delete item

print(person.keys())
print(person.values())
print(person.items())

# Loop through dict
for key, value in person.items():
    print(f"{key}: {value}")
