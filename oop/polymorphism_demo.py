import math

# Base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Formula for the area of a rectangle

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)  # Formula for the area of a circle
