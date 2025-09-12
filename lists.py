# # day 6 in python coding
# # Lists (Indexing, Slicing, Common Methods)
# # 1. indexing
# fruits = ["apple","banana", "cherry","guavas"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[-1])

# # 2. slicing
# print(fruits[0:2]) # ['apple', 'banana']
# print(fruits[::2]) # ['apple', 'cherry']
# print(fruits[2:]) # ['cherry', 'guavas'] 


# # 3. Append & insert
# fruits.append("orange")
# fruits.insert(3, "grapes")
# print(fruits)


# # 4. remove & pop
# fruits.remove("apple")
# print(fruits)
# last = fruits.pop()
# print("Popped:", last)

# # 5. Sorting & Reversing
# numbers = [5,2,6,9,1,7]
# numbers.sort()
# print(numbers)


# numbers.reverse()
# print(numbers)


# 📝 7 Exercises

# Create a list of 10 numbers and print the first 3 and last 3 elements.
digits = [1,2,3,4,5,6,7,8,9]
print(digits[6:])
print(digits[:3])

# Write a program to reverse a list without using .reverse() or slicing.

my_numbers = [1,5,8,9,4,7,3,2]


# Create a list of friends’ names and add two new names at specific positions.
names = ["Oscar","Precious","Joseph","Tendo","Arnold","David"]
names.append("Nathaniel")
names.insert(3, "Trent")
print(names)

# Remove all occurrences of a specific number from a list.

# Sort a list of numbers in ascending and descending order.
my_numbers = [1,5,8,9,4,7,3,2]
my_numbers.sort()
print(my_numbers)

my_numbers.reverse()
print(my_numbers)

# Use .count() to count how many times "apple" appears in a list.
my_food = ["apple","mango","orange","pawpaw"]
my_food.count("apple")
print(my_food.count("apple"))

# Write a program to merge two lists into one.
clubs = ["united","city","arsenal","real madrid","barcelona"]
prem = ["Spurs","chelsea","liverpool","Brighton"]
clubs.append(prem)
print(clubs)