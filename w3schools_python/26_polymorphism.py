# Python Polymorphism
# Same method name, different behavior

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"{type(shape).__name__}: area = {shape.area():.2f}")
