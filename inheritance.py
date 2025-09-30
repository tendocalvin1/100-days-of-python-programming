# object = A bundle of related attributes (variables) and methods(functions)
#          Example: phone, cup, book
#          You need a class to create objects


# class = A blueprint used to design the structure and layout of an object

# Revision on creating classes in python

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
        
    def drive(self):
        print(f"You drive the {self.year} {self.color} {self.model}")
        
        
    def stop(self):
        print(f"You stop the {self.year} {self.color} {self.model}")
        
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
        
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Tesla", 2024, "black", True)
car3 = Car("Mercedes Benz", 2024, "white", False)
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car3.drive()
car3.stop()
car3.describe()
        