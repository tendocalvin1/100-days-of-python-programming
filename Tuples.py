# tuples
# 1. Creating a tuple
person = ("Calvin", 22, "Uganda")
print(person[0]) # Calvin

# 2. tuple unpacking
name, age, country = person
print(name, age, country)

# 3. tuple immutability
# person[0] = "John" # Error (tuples can't be changed)

# sets
# 4. creating and using numbers
numbers = {1,2,3,4,5}
print(3 in numbers)


# 5. set operations
a = {1,2,3,4,5}
b = {3,4,5,6,7}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# 📝 7 Exercises

# Create a tuple with 5 items and print the second and fourth elements.
person1 = ("Exressions Oozing", 32, "United Kingdom", "Jamaica", "Youtuber")
name, age, country, origin , occupation = person1
print(age, origin)

# Use tuple unpacking to assign student details (name, age, course) to variables.
student = ("Tendo Calvin", 32 , "Computer Science")
name, age, cousrse = student
print(name, age, cousrse)

# Create two sets and print their union, intersection, and difference.
m = {1,2,3,4,5}
n= {3,4,5,6,7}

print(m.intersection(n))
print(m.union(n))
print(m.difference(b))

# Remove duplicates from a list using a set.


# Write a program to check if a number exists in a set.
my_nums = [1,2,3,4,5,6,7,8,9]
print(10 in my_nums)
print(5 in my_nums)
print(20 in my_nums)

# Create a set of vowels and use it to remove all vowels from a string.

# Create a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Word to process
word = "Uganda Christian University"

# Remove vowels
result = ''.join(ch for ch in word if ch not in vowels)

print("Original:", word)
print("Without vowels:", result)




# Write a program to find common elements between two lists using sets.

m = {1,2,3,4,5}
n= {3,4,5,6,7}
print(n.intersection(m))