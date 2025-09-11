# # Day 5 (Fri, 12 Sept): Strings Basics
# # 7 Examples involving strings

# # 1. String indexing & slicing
# text = "Python"
# print(text[0], text[-1], text[1: 4])

# # 2. String concatenation
# print("Hello" + " " + "World")

# # 3. String repetition
# print("Tendo Calvin SWE !" *3)

# # 4. Useful methods
# print("python".upper())
# print("PYTHON".lower())
# print(" hello ".strip())
# print("apple,banana,orange".split(","))

# # 5. String replacement
# print("I like Java".replace("Java", "Python"))

# # 6. Membership test
# print("Py" in "Python", "java" not in "Python")

# # 7. f-strings
# name, age = "Tendo calvin SWE", 23
# print(f"My name is {name} and I am {age} years old")


# Exercises
# number one
# Extract the first, middle, and last characters of a string.
numerals = "Calvin"
print(numerals[0], numerals[3], numerals[5])


# number two
# Reverse a string using slicing.
text = "Nathaniel"
print(text[2:5])

# number three
# Count how many times a word appears in a sentence.
sentence = "I am the best Software Engineer in East Africa"
print("Software" in sentence, "Tendo" in sentence)
print(sentence.count("best"))

# Write a program to check if a string is a palindrome.

# Convert a string to uppercase, lowercase, and title case.

# Split a string of comma-separated values into a list.

# Use f-strings to format a multiplication table for a number.

# Replace all vowels in a string with *.