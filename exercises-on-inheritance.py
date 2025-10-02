


# # 📘: Inheritance and Polymorphism**

# Focus: parent-child relationships, overriding, polymorphism.

# 1. Create an `Animal` base class with a method `speak()`.

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} is speaking and making a sound")
        
class Dog(Animal):
    
    def speak(self):
        print(f"{self.name} is barking")
        

class Cat(Animal):
    
    def speak(self):
        print(f"{self.name} is meowing")       

# dog = Dog("Max")
# cat = Cat("Rona")

# dog.speak()
# cat.speak()

class Bird(Animal):
    
    def speak(self):
        print(f"{self.name} is hissing.")
        
#bird = Bird("Ostrich")
#bird.speak()

animals = [Cat("Max"), Dog("Rona"), Bird("Ostrich")]

for animal in animals:
    print(f"{animal.speak()} speaks")
# 2. Make subclasses `Dog` and `Cat` that override `speak()`.
# 3. Add another subclass `Bird` with its own `speak()`.
# 4. Store all animals in a list and loop to call `speak()`.
# 5. Create a `Shape` base class with method `area()`.
# 6. Subclass it into `Circle`, `Square`, `Triangle`.
# 7. Override `area()` in each subclass.
# 8. Create a `Vehicle` base class with `drive()` method.
# 9. Subclass `Car` and `Bike` and override `drive()`.
# 10. Create a `Teacher` and `Student` class that inherit from `Person`.
# 11. Add attributes/methods specific to `Teacher` and `Student`.
# 12. Demonstrate `super()` to reuse parent code.
# 13. Write a `Calculator` class with `add` and `subtract`.
# 14. Subclass `AdvancedCalculator` with `multiply` and `divide`.
# 15. Show multiple inheritance with `Flyer` and `Swimmer` classes.
# 16. Create a `FlyingFish` class that inherits both.
# 17. Demonstrate operator overloading: define `__add__` in a `Vector` class.
# 18. Reflect: Why is polymorphism powerful in real-world software?