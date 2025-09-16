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
age = bool(input("How old are you ?"))
is_adult = age >= 18
print("Is adult:",is_adult) 

# is the person an adult
age = 15
is_adult = age >= 18
print("Is Adult:", is_adult)

# Example 2: Is the user logged in?
is_logged_in = False
print("Is logged in:", is_logged_in)

# Example 3: Has the student passed?

pass_mark = 48
passed = pass_mark >= 50
print("Has passed:", pass_mark)


# Example 4: Is it raining?
is_raining = True
print("Is rainig:", is_raining)


# Operators & Expressions (Day 4)

# Calculate the area and perimeter of a rectangle given length and width.

# Write a program that checks if a number is even or odd.

# Compute the compound interest given P, R, T.

# Strings (Day 5)

# Reverse a string input by the user.

# Count how many vowels are in a string.

# Take a sentence and print it in title case (each word capitalized).

# Ask the user for their first and last name and print their initials (e.g., John Doe → JD).

# Lists (Day 6)

# Create a list of 5 numbers. Print the largest and smallest numbers without using max() and min().

# Ask the user to input 5 names, store them in a list, and then print the list in reverse order.

# Write a program that removes duplicates from a list.

# Sum all elements in a list using a loop (without sum()).

# Tuples & Sets (Day 7)

# Create a tuple of 5 elements and print the 2nd and 4th elements.

# Write a program that finds the union and intersection of two sets of numbers.

# Check if a given element exists in a tuple or not.