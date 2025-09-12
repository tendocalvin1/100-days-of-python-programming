# day 6 in python coding
# Lists (Indexing, Slicing, Common Methods)
# 1. indexing
fruits = ["apple","banana", "cherry","guavas"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# 2. slicing
print(fruits[0:2]) # ['apple', 'banana']
print(fruits[::2]) # ['apple', 'cherry']
print(fruits[2:]) # ['cherry', 'guavas'] 


# 3. Append & insert
fruits.append("orange")
fruits.insert(3, "grapes")
print(fruits)


# 4. remove & pop
fruits.remove("apple")
print(fruits)
last = fruits.pop()
print("Popped:", last)

# 5. Sorting & Reversing
numbers = [5,2,6,9,1,7]
numbers.sort()
print(numbers)


numbers.reverse()
print(numbers)