# Write a program that asks the user for their name and age, then prints a greeting:
# Example: “Hello John, you are 20 years old.”

name = str(input("What is your name please ?"))
age = int(input("What is your age please ?"))
print(f"Hello, my name is {name} and I am {age} years old")

# Swap the values of two variables (without using a third variable).
# numbers 
a = 10
b = 15
a, b = b, a

print(a, b)

# Take two numbers from the user and print their sum, difference, product, and quotient.

number_one = int(input("Enter the first number please:"))
number_two = int(input("Enter the second number please:"))

print(f"The sum of these two numbers is :", number_one + number_two)
print(f"The difference of these two numbers is :", number_one - number_two)
print(f"The product of these two numbers is :", number_one * number_two)
print(f"Result from the division between these two numbers is :", number_one / number_two)


# Data Types (int, float, str, bool) 

# Check the data type of a user’s input and print whether it’s a string, int, or float.
print(type ("Tendo calvin"))
print(type (5))
print(type (2.65))

# Convert temperature from Celsius to Fahrenheit.
celsius = 0
Fahrenheit = (celsius * 1.8) + 32
print(f"The temperatre in Fahrenheit is:", Fahrenheit)


# Create a Boolean variable is_adult that is True if age ≥ 18, otherwise False.

age1 = int(input("Enter your age please:"))

if age1 >= 18:
    print("You are an adult, you can now start living alone")
    
else:
    print("You are still young to get married and have kids.")