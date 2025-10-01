# polymorphism = Greek word that means "to have many forms or faces"
#               Poly = Many
#               Morphe = Form

# Two ways to achieve Polymorphism
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, width):
        self.width = width
        
    def area(self):
        return self.width * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    
    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    
    def area(self):
        return self.length * self.width
        


shapes = [Circle(5), Square(10), Triangle(4, 8), Rectangle(10, 15)]

for shape in shapes:
    print(f"{shape.area()}")