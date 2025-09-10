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