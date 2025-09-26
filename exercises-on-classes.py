# Classes in OOP(Python)
# Backend Engineering, Data Science, Machine Learning and Artificial Intelligence


# Focus: creating classes, attributes, and objects.

# 1. Create a class `Car` with attributes `brand` and `model`.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

    def drive(self):
        print("The car is driving")
        
        
motorcar = Car("Bugatti", "Veron")

# Accessing attributes
print("Brand:", motorcar.brand)
print("Model:", motorcar.model)
        
        
           
# 2. Instantiate 3 different car objects.
motorvehicle = Car("Toyota", "harrier")
motorcycle = Car("Honda", "TMX")

# Accessing attributes
print("Brand:", motorvehicle.brand)
print("Model:", motorvehicle.model)

print("Brand:", motorcycle.brand)
print("Model:", motorcycle.model)





# 3. Add a method `drive()` that prints `"The car is driving"`.
motorcar.drive()
motorvehicle.drive()
motorcycle.drive()

# 4. Create a class `Book` with title and author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def summary(self):
        print(self.title, self.author)

# 5. Make objects for 3 books and print their details.
Book1 = Book("Elon Musk, The Respected Man in tech", "Walter Isaacson")
Book2 = Book("Steve Jobs, The Respected Man in tech", "Walter Isaacson")
Book3 = Book("Good to Creat", "Jim Collins")

print(Book3.author)
print(Book3.title)

Book1.summary()
Book2.summary()
Book3.summary()

# 6. Add a method `summary()` to `Book` that prints title and author.
# 7. Create a `Person` class with attributes `name` and `age`.
# 8. Write a method `birthday()` that increases age by 1.
# 9. Create 5 different `Person` objects and store them in a list.
# 10. Loop through the list and call `birthday()` for each.
# 11. Write a `Rectangle` class with `length` and `width`.
# 12. Add a method `area()` to compute area.
# 13. Add a method `perimeter()`.
# 14. Create multiple rectangles and compare their areas.
# 15. Create a `Laptop` class with brand, RAM, and storage.
# 16. Add a method `specs()` that prints all attributes.
# 17. Instantiate a `Laptop` and call `specs()`.