# Dictionaries (CRUD Operations, Methods)
# 1. create dictionary
student = {"name": "Calvin", "age": 22, "course": "Computer Science"}
print(student["name"])

# 2. update value
student["age"] = 23
print(student)

# 3. add new key-value pair
student["profession"] = "Software Engineer"
print(student)

# 4. delete a key
del student["age"]
print(student)


# 5. dictionary methods
print(student.keys())   # (['name', 'course', 'profession'])
print(student.values()) # (['Calvin', 'Computer Science', 'Software Engineer'])
print(student.items())  # ([('name', 'Calvin'), ('course', 'Computer Science'),
                        #('profession', 'Software Engineer')])
                     
                        

# 📝 7 Exercises

# Create a dictionary with details about your favorite movie (title, year, genre, rating).
movie = {"title": "Expendables", "year": 2014, "genre": "Adults", "rating": 4.6}
print(movie)
# Write a program to update a dictionary with a new key-value pair.
movie["producer"] = "Tyler Perry"
print(movie)

# Remove a key from a dictionary and print the updated dictionary.

del movie["producer"]
print(movie)

# Loop through a dictionary and print all keys and values separately.
print(movie.keys())
print(movie.items())
print(movie.values())


# Merge two dictionaries into one.
movie = {"title": "Expendables", "year": 2014, "genre": "Adults", "rating": 4.6}
student = {"name": "Calvin", "age": 22, "course": "Computer Science"}

merged = {**movie, **student}
print(merged)


# Write a program to count the frequency of each word in a given sentence using a dictionary.
# Sentence
sentence = "Python is great and Python is fun"

# Convert to lowercase (optional, for uniformity)
sentence = sentence.lower()

# Split into words
words = sentence.split()

# Create empty dictionary
frequency = {}

# Count word frequencies
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Print results
print("Word Frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")


# Store marks of 5 students in a dictionary and print the student with the highest score.
scholars = {"student1": 50, "student2": 70, "student3": 80, "student4": 85, "student5": 68,}
print(scholars["student4"])