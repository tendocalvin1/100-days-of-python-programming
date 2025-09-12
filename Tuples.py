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