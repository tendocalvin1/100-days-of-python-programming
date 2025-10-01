# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed
#                 They can contain abstract methods, which are declared but have no implementation
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the class itself
#                 2. Requires children to use inherited abstract methods

# To use abstraction, we need to use abc
# abc = abstract base class

from abc import ABC , abstractmethod

class Vehicle(ABC):
    
 
    @abstractmethod
    def go(self):
        pass
    
    
    @abstractmethod
    def stop(self):
        pass
    
    
class Car(Vehicle):
    
     def go(self):
        print("You drive the car")
    
     def stop(self):
        print("You stop the car")
        

car1 = Car()
car1.go()
car1.stop()
   
   
   
class Motorcycle(Vehicle):
    
    def go(self):
        print("You drive the motorcycle")
    
    def stop(self):
        print("You stop the motorcycle")
        
motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()