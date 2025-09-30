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


# class variables = Shared among all instances of a class 
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    
    class_year = 2025
    num_students = 0
    def __init__(self, name , age, profession):
        self.name = name
        self.age = age
        self.profession = profession
        Student.num_students += 1
        
student1 = Student("Tendo Calvin", 23, "Software Engineer")
student2 = Student("David Beckham", 50, "Footballer")
student3 = Student("Aaron Ramsey", 35, "Footballer")

print(student1.profession)
print(student1.name)
print(student1.age)    
print(Student.class_year)
print(Student.num_students) 
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")  