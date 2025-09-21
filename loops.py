# loops in python programming
# while loop
# a while loop executes some code while some condition remains True

# example one
name = input("Enter your name:")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name:")

print(f"Hello,{name}!")

# example two
age = int(input("Enter your age please:"))

while age <= 0:
    print("Invalid age. Age is strictly positive.")
    age = int(input("Enter your age please:"))
    
print(f"You are {age} years old.")


#example three
food = input("Enter a food you like (q to quit):")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit):")
    
print("Goodbye!")


# logical operators in while loops
# example one
number = int(input("Enter a # between 1 - 10"))

while number < 1 or number > 10:
    print(f"{number} is not between 1 and 10")
    number = int(input("Enter a # between 1 - 10")) 

print(f"Your number is {number} and it is between 1 - 10")    


# for loop
# a for loop 
