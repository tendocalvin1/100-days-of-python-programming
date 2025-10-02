


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

class Shape:
    def area(self):
        pass
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    
    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, width):
        self.width = width
        
    def area(self):
        return self.width **2

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return 0.5 * self.width * self.height
    

shapes = [Circle(5), Square(8), Triangle(4, 20)]

for shape in shapes:
    print(f"{shape.area()}")
# 6. Subclass it into `Circle`, `Square`, `Triangle`.
# 7. Override `area()` in each subclass.
# 8. Create a `Vehicle` base class with `drive()` method.

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def drive(self):
        pass
    
class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
        
    def drive(self):
        print(f"The {self.color} {self.brand} is being driven by the rich fella")
        
        
class Bike(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
        
    def drive(self):
        print(f"The {self.color} {self.brand} is being driven by Elon Musk")
        
car = Car("Tesla", "red")
bike = Bike("BMX", "black")

car.drive()
bike.drive()
# 9. Subclass `Car` and `Bike` and override `drive()`.
# 10. Create a `Teacher` and `Student` class that inherit from `Person`.

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        
    def description(self):
        print(f"My name is {self.name} and I come from {self.country}")
        
class Teacher(Person):
    def __init__(self, name, age, country):
        super().__init__(name, age, country)
        
    def description(self):
        print(f"My name is {self.name} and during my leisure time, I do some farming")
        
        
class Student(Person):
    def __init__(self, name, age, country):
        super().__init__(name, age, country)
        
    def description(self):
        print(f"My name is {self.name} and I want to be the best SWE in the world with various tools")
        

teacher = Teacher("David Beckham", 50, "United Kingdom")
student = Student("Tendo Calvin", 23, "Uganda")

teacher.description()
student.description() 

print(student.name) 
print(student.age) 
print(student.country)      

# 11. Add attributes/methods specific to `Teacher` and `Student`.
# 12. Demonstrate `super()` to reuse parent code.
# 13. Write a `Calculator` class with `add` and `subtract`.

class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self):
        return self.number + self.number
        
    def subtract(self):
        return self.number - self.number
    
class AdvancedCalculator(Calculator):
    def __init__(self, number):
        super().__init__(number)
        
    def multiply(self):
        return self.number * self.number
    
    
    def divide(self):
        return self.number / self.number
    
calculator = Calculator(10)
advancedCalculator = AdvancedCalculator(10)

print(advancedCalculator.subtract())
# 14. Subclass `AdvancedCalculator` with `multiply` and `divide`.
# 15. Show multiple inheritance with `Flyer` and `Swimmer` classes.

class Flyer:
    def __init__(self, name):
        self.name = name
        
    def flying(self):
        print(f"{self.name} is flying")
        
class Swimmer:
    def __init__(self, name):
        super().__init__(name)
        
    def swimming(self):
        print(f"{self.name} is swimming")
        

class FlyngFish(Flyer, Swimmer):
    pass

flyingFish = FlyngFish("Tuna")

flyingFish.swimming()
flyingFish.flying()
# 16. Create a `FlyingFish` class that inherits both.
# 17. Demonstrate operator overloading: define `__add__` in a `Vector` class.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operator overloading for +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # For pretty printing
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Demonstration
v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2   # This calls v1.__add__(v2)
print(v3)      # Output: Vector(6, 4)

# 18. Reflect: Why is polymorphism powerful in real-world software?


## 🔹 Why is polymorphism powerful in real-world software?

# Polymorphism means **“many forms”** — in programming, it’s the ability for different classes to provide a **common interface** (same method names), while each class implements the method in its own way.

# ### ✅ Real-world benefits:

# 1. **Flexibility & Extensibility**

#    * You can write code that works with **different object types** without knowing their exact class.
#    * Example: A `start()` method for `Vehicle` can be applied to `Car`, `Bike`, or `Bus`, each starting differently. If later you add `ElectricCar`, it still works without changing existing code.

# 2. **Code Reuse**

#    * You don’t need to rewrite logic for each new class.
#    * Example: A function `make_it_fly(flyer)` can work for `Bird`, `Airplane`, or `Superhero` — as long as they implement `fly()`.

# 3. **Improved Maintainability**

#    * Changes are localized. If you need to update how `Motorcycle.start()` works, you only change that method, not everywhere motorcycles are used.

# 4. **Supports Abstraction**

#    * You can focus on *what* an object does, not *how* it does it.
#    * Example: A payment system can call `process_payment()` on `CreditCard`, `PayPal`, or `CryptoWallet` without worrying about the internal logic.

# 5. **Encourages Scalable Design (Open/Closed Principle)**

#    * Systems built with polymorphism are open to extension (new types), but closed to modification (no need to edit old code).
#    * This makes software scalable and adaptable to new requirements.

# ---

# ### 🌍 Real-world analogy

# Think of a **universal remote**:

# * It has one “play” button (common interface).
# * Whether it’s a TV, DVD player, or speaker, pressing “play” works — but the action is different depending on the device.
# * That’s polymorphism in everyday life!

# ---

# ✅ **In short:** Polymorphism is powerful because it allows software to be **flexible, reusable, scalable, and easier to maintain**, which is exactly what you need in large, real-world projects.

# ---

