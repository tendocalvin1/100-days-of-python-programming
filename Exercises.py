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