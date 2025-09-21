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


# more examples of functions using the python

# factorial with recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial_recursive(n -1)
    
print(factorial_recursive(6))


# function returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3,6,9,12])

print(low, high)

# function taking a list and looping
def squared_list(numbers):
    squared = []
    for n in numbers:
        squared.append(n ** 2)
    
    return squared 

print(squared_list([2, 4])) 


# exercises on functions

# Simple Greeting: Write a function hello_user(name) that prints "Hello, <name>!".
def hello_user(name):
    print(f"hello,{name}!")
    
hello_user("Tendo")

# Even or Odd: Write a function is_even(n) that returns True if n is even, otherwise False.

def is_even(number):
    if number % 2 == 0:
        return True
    
    else:
        return False
    
print(is_even(15))
print(is_even(20))
print(is_even(25))

# Sum of List: Write a function sum_list(numbers) that returns the sum of all numbers in a list.

def sum_list(numbers):
    return sum(numbers)
    
print(sum_list([2,3,4,5,6]))

# Max of Three: Write a function max_of_three(a, b, c) that returns the largest of three numbers.

def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(3,2,5))

# Word Count: Write a function count_words(sentence) that counts how many words are in a sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("My name is Tendo Calvin and I am the best Software Engineer in the world."))

# Prime Number Check: Write a function is_prime(n) that checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

# Temperature Converter: Write a function celsius_to_fahrenheit(c) that converts Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(celsius_to_fahrenheit(0))
