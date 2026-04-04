# ============================================================
#          PYTHON DICTIONARIES - CORE CONCEPTS
# ============================================================

# ----------------------------------------------------------
# 1. WHAT IS A DICTIONARY?
#    - Stores data as KEY: VALUE pairs
#    - Keys must be UNIQUE and IMMUTABLE
#    - Values can be ANYTHING
# ----------------------------------------------------------

# Creating a dictionary
student = {
    "name": "Aditya",
    "age": 20,
    "grade": "A",
    "city": "Delhi"
}
print("Dictionary:", student)


# ----------------------------------------------------------
# 2. ACCESSING VALUES
#    - Use the KEY inside square brackets []
#    - Or use .get() which is safer (no crash if key missing)


print("\n--- ACCESSING VALUES ---")
print("Name:", student["name"])          # Direct access
print("Age:", student.get("age"))        # Using .get()
print("Phone:", student.get("phone", "Not Found"))  # Default value if key missing


# ----------------------------------------------------------
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


# ----------------------------------------------------------
# 6. LOOPING THROUGH A DICTIONARY
# ----------------------------------------------------------

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


# ----------------------------------------------------------
# 8. DICTIONARY COMPREHENSION
#    - Create a dictionary in ONE line (like list comprehension)
# ----------------------------------------------------------

print("\n--- DICTIONARY COMPREHENSION ---")

# Create a dict of number: square
squares = {num: num**2 for num in range(1, 6)}
print("Squares:", squares)

# Filter: only even numbers
even_squares = {num: num**2 for num in range(1, 11) if num % 2 == 0}
print("Even Squares:", even_squares)


# ----------------------------------------------------------
# SUMMARY
# ----------------------------------------------------------
# dictionary = {key: value}        → Create
# dict[key]                        → Access
# dict[key] = value                → Add/Update
# del dict[key]                    → Delete
# key in dict                      → Check
# dict.keys(), .values(), .items() → View
# for k, v in dict.items()         → Loop
# ============================================================