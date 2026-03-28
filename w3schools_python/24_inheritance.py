# Python Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
print(isinstance(dog, Animal))  # True

# super()
class Puppy(Dog):
    def __init__(self, name, toy):
        super().__init__(name)
        self.toy = toy

puppy = Puppy("Max", "ball")
print(puppy.speak())
print(puppy.toy)
