# # Day two of 100 days of python code
# # integers [Whole numbers, positive or negative without decimals]
# age = 23
# year = 2025
# temperature = -7

# print(age)
# print(year)
# print(temperature)

# # Float [Numbers with decimal points]
# pi = 3.14159
# price = 19.99
# height = 1.75

# print(pi)
# print(price)
# print(height)


# # Strings (str)
# # Text enclosed in single '' or double " " quotes
# name = "Tendo Calvin SWE"
# city = "Mukono"
# greeting = "Hello, world !"


# # Boolean(bool)
# # Represents True or False
# # Used for conditions, logic or comparisons
# is_raining = True
# has_license = False
# passed_exam = True

# number one
name = "Calvin"
age = 20
height = 1.75
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# number two
number_one = int(input("Enter your favourite number(int):"))
number_two = float(input("Enter the second number(float):"))
print(f"The result of both numbers that is number one & number two is:", number_one + number_two)


# number three
age = 15
if age >= 18:
    print("Eligible to vote")
    
else:
    print("Still very young to vote")
    

# number 4
item1 = int(input("Enter the price of Rice"))
item2 = float(input("Enter the price of pork"))
print("The total price of both items is:", item1 + item2)

# number 5
# Ask the user for their name and height
user = input("What is your name please? ")
height = float(input("What is your height in meters please? "))

# Check if the height is greater than 1.6
is_tall = height > 1.6

# Print the result
print(user, "Height greater than 1.6 meters:", is_tall)
