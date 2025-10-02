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
    
    
# Duck typing = Another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck"


class Animal:
    alive = True
    

class Dog(Animal):
    def speak(self):
        print("WOOF !")
        

class Cat(Animal):
    def speak(self):
        print("MEOW !")
        
        
class Car:
    alive = False
    def speak(self):
        print("HORN !")
        
        
animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
    
    

# Aggregation = Represents a relationship where one object(the whole) contains references
#               to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    
    def list_book(self):
        return [f"{book.title} by {book.author}" for book in self.books ]
        
        
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
library = Library("UCU Public Library")

book1 = Book("Diary of a ceo", "Steve Bartlett") 
book2 = Book("Good to Great", "Jim Collins") 
book3 = Book("How The Mighty Fall", "Jim Collins") 


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_book():
    print(book)
    
    
# composition = The composed object directly owns its components, which cannot exist independently
#               "owns a relationship"

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
        
class Wheel:
    def __init__(self, size):
        self.size = size
        
class Vehicle:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
        
    def description(self):
        return f"{self.make} {self.model}  {self.engine.horse_power}(hp) {self.wheels[0].size}inch"
        

vehicle1 = Vehicle("Ford", "Mustang", 500, 18)
vehicle2 = Vehicle("Toyota", "Harrier", 650, 19)

print(vehicle1.description())
print(vehicle2.description())
