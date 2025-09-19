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