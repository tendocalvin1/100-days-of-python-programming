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
#name = input("Enter your name please:")
#print("My name is:", name)

# By default, input is read as a string. If you want numbers, you must convert:
#age = int(input("Enter your age please:")) # converts input to string
#print("I shall be", age + 1, "years old next year.")


# output in python
# we use print for output in python
#name = "Tendo Calvin SWE"
#score = 90
#print(f"Hello {name}, your score is {score}")




# Exercises
# 1. Greeting program
# name = input("Enter your name please:")
# print(f"Hello {name}, welcome to python programming.")

# # 2. Age in 5 years.
# age = int(input("Enter the age:"))
# print("I shall be", age + 5,"in the next 5 years")

# # simple calculator
# number_one = int(input("Enter the first number:"))
# number_two = int(input("Enter the second number:"))

# print(f"The sum of these two numbers is:",number_one + number_two)
# print(f"The product of these two numbers is:",number_one * number_two)
# print(f"The result of the division of these two numbers is:",number_one / number_two)
# print(f"The result from the subtraction of these two numbers is:",number_one - number_two)

# Area of a rectangle
# length = int(input("Enter the length:"))
# width = int(input("Enter the width:"))
# area = length* width
# print(f"The area of the rectangle is {area} cm\u00b2")


# Temperature converter
# Temps_in_celsius = int(input("Enter the degrees(temps):"))
# temps_in_fahreinheit = (Temps_in_celsius * 1.8) + 32
# print(f"The temps from celsius to fahreinheit are:", temps_in_fahreinheit)



# even or odd number
# number = int(input("Enter a digit:"))
# if number % 2 == 0:
#     print("This is an even number")

# else:
#     print("This is an odd number")

# Swapping Variables
# Write a program that swaps the values of two variables. (e.g., a=5, b=10 → after swap → a=10, b=5)

a = 5
b = 10
a, b = b, a  # swap values
print("a =", a, "b =", b)

# Simple Interest Calculator
# Ask for principal, rate, and time, then calculate Simple Interest using:
# SI = (P × R × T) / 100

pricipal = 500
rate = 0.5
time = 3

simple_interest = pricipal * rate * time
print(f"The simple interest from this man's account is:", simple_interest)