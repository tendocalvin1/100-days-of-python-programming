# variables in python
# A variable is simply a name that stores a value in  memory
# Think of variables like a box with a label
# You can store different types of values("numbers, text, etc");


name = "Tendo"
age = 23
height = 1.65


print("Name:", name)
print("age:", age)
print("height:", height)


# input in python
# The input() function allows  the user to type something from the keyboard
name = input("Enter your name please:")
print("My name is:", name)

# By default, input is read as a string. If you want numbers, you must convert:
age = int(input("Enter your age please:")) # converts input to string
print("I shall be", age + 1, "years old next year.")