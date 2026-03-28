# Python Classes and Objects

class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name           # Instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def __str__(self):
        return f"Dog({self.name}, {self.age})"

dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

print(dog1.bark())
print(dog2.name)
print(dog1.species)
print(dog1)
