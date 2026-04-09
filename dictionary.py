
# 1. WHAT IS A DICTIONARY?
#    - Stores data as KEY: VALUE pairs
#    - Keys must be UNIQUE and IMMUTABLE
#    - Values can be ANYTHING


# Creating a dictionary
student = {
    "name": "Aditya",
    "age": 20,
    "grade": "A",
    "city": "Delhi"
}
print("Dictionary:", student)



# 2. ACCESSING VALUES
#    - Use the KEY inside square brackets []
#    - Or use .get() which is safer (no crash if key missing)


print("\n--- ACCESSING VALUES ---")
print("Name:", student["name"])          # Direct access
print("Age:", student.get("age"))        # Using .get()
print("Phone:", student.get("phone", "Not Found"))  # Default value if key missing


# 3. ADDING AND UPDATING VALUES
#    - Assign a new key to ADD
#    - Assign to existing key to UPDATE


print("\n--- ADDING & UPDATING ---")
student["phone"] = "9999999999"     # ADD a new key
student["age"] = 21                 # UPDATE existing key
print("Updated Dictionary:", student)


# ----------------------------------------------------------
# 4. REMOVING VALUES
#    - del keyword: removes a specific key
#    - .pop(): removes and RETURNS the value
#    - .clear(): removes ALL items


print("\n--- REMOVING VALUES ---")
removed = student.pop("city")       # Removes "city" and returns its value
print("Removed city:", removed)
print("After pop:", student)

# 5. USEFUL DICTIONARY METHODS
# ----------------------------------------------------------

print("\n--- USEFUL METHODS ---")

# .keys() - all keys
print("Keys:", list(student.keys()))

# .values() - all values
print("Values:", list(student.values()))

# .items() - all key-value pairs as tuples
print("Items:", list(student.items()))

# Check if a key exists
print("Is 'name' in student?", "name" in student)
print("Is 'address' in student?", "address" in student)

# Length of dictionary
print("Total fields:", len(student))


# 6. LOOPING THROUGH A DICTIONARY


print("\n--- LOOPING ---")

# Loop through keys
for key in student:
    print(f"Key: {key}")

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key} --> {value}")

# ----------------------------------------------------------
# 7. NESTED DICTIONARY
#    - A dictionary INSIDE a dictionary

print("\n--- NESTED DICTIONARY ---")

classroom = {
    "student1": {"name": "Aditya", "marks": 95},
    "student2": {"name": "Rahul", "marks": 88},
    "student3": {"name": "Priya", "marks": 92},
}

# Accessing nested value
print("Student1 Name:", classroom["student1"]["name"])
print("Student2 Marks:", classroom["student2"]["marks"])

# Loop through nested dictionary
for student_id, info in classroom.items():
    print(f"{student_id}: {info['name']} scored {info['marks']}")


# 8. DICTIONARY COMPREHENSION
#    - Create a dictionary in ONE line (like list comprehension)


print("\n--- DICTIONARY COMPREHENSION ---")

# Create a dict of number: square
squares = {num: num**2 for num in range(1, 6)}
print("Squares:", squares)

# Filter: only even numbers
even_squares = {num: num**2 for num in range(1, 11) if num % 2 == 0}
print("Even Squares:", even_squares)



# dictionary = {key: value}        → Create
# dict[key]                        → Access
# dict[key] = value                → Add/Update
# del dict[key]                    → Delete
# key in dict                      → Check
# dict.keys(), .values(), .items() → View
# for k, v in dict.items()         → Loop


#Question

# Easy: Dictionary Basics
# - Create a dictionary representing a student with keys: name, age, grade, and city.
# - Print the student's name and age.
# - Add a new key "phone" with a value of your choice.
# - Update the "grade" to a new value.
# - Remove the "city" key.
# - Loop through the dictionary and print all key-value pairs.
# - Check if a specific key exists in the dictionary.
# - Find the total number of key-value pairs.
# - Use dictionary comprehension to create a dictionary of squares for numbers 1 to 5.
# - Create a nested dictionary representing a classroom with multiple students and their marks.

# Medium: Dictionary Operations
# - Given two dictionaries, merge them into a single dictionary.
# - Count the frequency of each character in a given string using a dictionary.
# - Find the most common element in a list using a dictionary.
# - Given a list of numbers, create a dictionary where keys are the numbers and values are their squares.
# - Implement a simple inventory system using a dictionary (item: quantity).
# - Check if two dictionaries are equal.
# - Given a dictionary, create a new dictionary with keys and values swapped.
# - Use dictionary comprehension to filter a dictionary based on some condition.
# - Create a dictionary of employee records with nested dictionaries for personal and professional details.
# - Implement a function to find the second largest value in a dictionary.

# Hard: Advanced Dictionary Problems
# - Implement a function to find the longest word in a dictionary of words.
# - Given a list of dictionaries, group them by a specific key.
# - Implement a function to find the intersection of two dictionaries (common keys with same values).
# - Given a dictionary, create a new dictionary where keys are sorted alphabetically.
# - Implement a function to find the most frequent key in a dictionary.
# - Given a dictionary, create a new dictionary where values are the sum of all values in the original dictionary.
# - Implement a function to find the longest substring without repeating characters using a dictionary.
# - Given a dictionary, create a new dictionary where keys are the values and values are the keys.
# - Implement a function to find the most frequent character in a string using a dictionary.
# - Given a dictionary, create a new dictionary where keys are the values and values are the keys.

#easy questions 
# - Create a dictionary representing a student with keys: name, age, grade, and city.
student={
    "name":"Aditya",
    "age":20,
    "grade":"A",
    "city":"Delhi"
}
print(student)

print(student["name"])
print(student["age"])

student["phone"]="9999999999"
print(student)

student["grade"]="A+"
print(student)

del student["city"]
print(student)

## - Loop through the dictionary and print all key-value pairs.
for i in student:
    print(i)

# - Check if a specific key exists in the dictionary.
print("name" in student)

# - Find the total number of key-value pairs.
print(len(student))

# - Use dictionary comprehension to create a dictionary of squares for numbers 1 to 5.
squares = {num: num**2 for num in range(1, 6)}
print(squares)

# - Create a nested dictionary representing a classroom with multiple students and their marks.
classroom = {
    "student1": {"name": "Aditya", "marks": 95},
    "student2": {"name": "Rahul", "marks": 88},
    "student3": {"name": "Priya", "marks": 92},
}
print(classroom)    

#medium questions 

# - Given two dictionaries, merge them into a single dictionary.


