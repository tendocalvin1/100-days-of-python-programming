# A class is a blueprint for creating objects. It defines attributes(data) and methods(functions)
# that the objects created from the class can have

# Think of a class as a template, and an object as an instance of that class.
# Classes allow object oriented programming concepts like encapsulation, inheritance and
# polymorphism. 

# Examples 

class Dog:
    # class attribute
    species = "canis familiaris"
    
    # constructor (initializes object attributes)
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
        
# method
    def bark(self):
        return f"{self.name} says woof"

# creating an object (instance) of the class
my_dog = Dog("David", 4)

print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())




class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"
    
    
my_cat = Cat("Dean", 8)
print(my_cat.speak())


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
        
    def information(self):
        return f"{self.brand} {self.model} , {self.year}"
        

car1 = Car("Tesla", "EV", 2025)
print(car1.information())


# Student class 
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_pass(self):
        return self.grade >= 50

student1 = Student("Alice", 75)
student2 = Student("Bob", 40)

print(student1.is_pass())  # True
print(student2.is_pass())  # False



# 5. Exercises

# Exercise 1: Create a class Rectangle with attributes length and width, and a method area that returns the area of the rectangle.

# Exercise 2: Create a class BankAccount with:

# Attributes: owner, balance

# Methods: deposit(amount), withdraw(amount)

# Make sure withdraw does not allow balance to go negative.

# Exercise 3: Create a class Book with:

# Attributes: title, author, pages

# Method: description() → prints “Title by Author, Pages pages”

# Exercise 4 (Challenge): Create a Circle class with:

# Attribute: radius

# Methods:

# area()

# circumference()

# Hint: Use pi = 3.14159

# Exercise 5 (Inheritance): Create a parent class Vehicle with method start(). Then create a child class Motorcycle that overrides the start() method to print “Motorcycle started.”












