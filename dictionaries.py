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