# day 3 0f 100 days of code

# 1. arithmetic operators
x, y = 10, 3
print(x+y, x - y, x * y, x / y, x // y, x % y, x**y)

# 2. comparison operators [true or false]
print(x > y, x >= y, x == y, x != y, x <= y)

# 3. logical operators
a , b = True, False
print(a  and b, b and a, b or a, a or b)


# 4. Assignment operators
n = 5
n += 3
print("After +=3:", n)


# 5. Bitwise operators
print(5 & 3, 5 |3 , 5 ^3 , ~5, 5 << 1)

# 6. Membership operators
nums = [1, 2, 3, 4]
print(2 in nums, 5 not in nums)


# 7. Identity operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b, a is not c, a == c)

# exercises
number1 = int(input("Enter a number:"))
number2 = int(input("Enter a number:"))

print(f"The sum of these two numbers is:", number1 + number2)
print(f"The difference between these two numbers is:", number1 - number2)
print(f"The product of these two numbers is:", number1 * number2)
print(f"Divsion:", number1 / number2)


# number two
# Write a program to check if a number is even and greater than 10.
digit = int(input("Enter a digit please:"))
if (digit % 2 == 0 and digit >= 10):
    print("The number is both even and above 10")
    
else:
    print("The entered number doesnot meet the required requirements")
    
# number three
# Use assignment operators to update a variable’s value in multiple steps.
m = 10
n = 12
m , n = n , m
print(m ,n)


# number four
# Check if a given character is present in a string

names = ["Tendo", "Calvin","Arnold","Reagan","Nathaniel"]
print("Tendo" in names, "Melissa" not in names)

# Number 5
# Demonstrate bitwise operations on two integers.

c = 12
d = 15
print(c >> d, ~d, 12 |15, 12 & 15)

# number 6
# Write a program to compare two numbers entered by the user.
nums1 = int(input("Enter the number:"))
nums2 = int(input("Enter the second number:"))

print(nums1 > nums2, nums1 == nums2, nums1 != nums2 , nums2 <= nums1)

# number 7
# Use logical operators to check if a number is between 10 and 20.
number = int(input("Enter the number please:"))
if (number >= 10 and number <=20) :
    print("The number meets the requirements")
    
else:
    print("Number not between 10 and 20.")
    
    
# number 8
# Show the difference between is and == using lists.
clubs = ["Madrid", "PSG", "Juventus", "Barcelona","Dortmund"]
channels = ["DR Sports", "That's Football", "Aftv", "United Stand"]

print(clubs is channels, clubs == channels)

# 🔹 == (Equality operator)
# Checks whether the contents of two objects are the same.
# Example: if two lists have the same elements in the same order, == will return True, even if they are stored in different memory locations.


# 🔹 is (Identity operator)
# Checks whether two variables actually point to the same object in memory.
# Even if two lists look identical, is will only return True if they’re literally the same object, not just equal in value.


# ⚠️ Key takeaway with lists
# == → compares values (what’s inside the list).
# is → compares memory identity (are they the exact same list object).






