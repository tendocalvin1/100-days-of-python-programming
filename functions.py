# functions in python
# A function is a reusable block of code that performs a specific task
# examples
def greet():
    print("hello, welcome to python programming. A language known for its versatility.")

greet()  

def greet_user(name):
    print(f"Hello,{name}!")
    
greet_user("Tendo")

# function that returns a value
def add_numbers(a, b):
    print(f"The sum of these two numbers is:", a + b)

add_numbers(5, 6)

# function with default parameter
def power(base, exponent=2):
    print(base ** exponent)

power(3)

# function with multiple return values
def calculate(a, b):
    sum_result = a + b
    difference = a - b
    print(sum_result, difference)
    
calculate(6, 4)

# Exercises on Functions in python
# Write a function square(num) that takes a number and returns its square.

def square(number):
    print(number ** 2)

square(6)
square(4)

# Write a function is_even(num) that returns True if a number is even, otherwise False.
def is_even(num):
    if num % 2 == 0:
        print("The number is even")
        
    else:
        print("The number is odd")
        
is_even(3)
is_even(4)

# Write a function factorial(n) that calculates the factorial of a number.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *=1
    return result
    
factorial(5)
print(factorial(5))

    
#     # looping through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# Write a function reverse_string(text) that returns the string reversed.

def reverse_string(text):
    return text[::-1]

reverse_string("manchester united")
print(reverse_string("manchester united"))

# Write a function average(numbers) that takes a list of numbers and returns their average.

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(average([2,3,4,5,6,7,8]))

 