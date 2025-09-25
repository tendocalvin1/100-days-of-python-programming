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













