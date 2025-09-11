# Day 5 (Fri, 12 Sept): Strings Basics
# 7 Examples involving strings

# 1. String indexing & slicing
text = "Python"
print(text[0], text[-1], text[1: 4])

# 2. String concatenation
print("Hello" + " " + "World")

# 3. String repetition
print("Tendo Calvin SWE !" *3)

# 4. Useful methods
print("python".upper())
print("PYTHON".lower())
print(" hello ".strip())
print("apple,banana,orange".split(","))

# 5. String replacement
print("I like Java".replace("Java", "Python"))

# 6. Membership test
print("Py" in "Python", "java" not in "Python")

# 7. f-strings
name, age = "Tendo calvin SWE", 23
print(f"My name is {name} and I am {age} years old")