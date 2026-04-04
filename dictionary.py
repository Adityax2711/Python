
#  PYTHON DICTIONARIES - CORE CONCEPTS
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

# 4. REMOVING VALUES
#    - del keyword: removes a specific key
#    - .pop(): removes and RETURNS the value
#    - .clear(): removes ALL items


print("\n--- REMOVING VALUES ---")
removed = student.pop("city")       # Removes "city" and returns its value
print("Removed city:", removed)
print("After pop:", student)

# 5. USEFUL DICTIONARY METHODS

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

# 6. LOOPING THROUGH A DICTIONAry

print("\n--- LOOPING ---")

# Loop through keys
for key in student:
    print(f"Key: {key}")

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key} --> {value}")

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

#easy questions 
#1. Create & Access Create a dictionary with your name, age, and city. Print each value using its key.
    #2. Update a Value Create a dictionary {"item": "pen", "price": 10}. Update the price to 15 and print it.
#3. Add & Delete Start with {"a": 1, "b": 2, "c": 3}. Add key "d": 4, then delete key "b". Print the result.
#4. Check if Key Exists Write a program that checks if "email" exists in a student dictionary. Print "Found" or "Not Found".
#5. Count Items Create a dictionary with 5 fruits and their prices. Print how many items are in the dictionary using len().


#medium questions
#6. Loop & Print Given a dictionary of 5 students and their marks, loop through and print: "Aditya scored 95 marks"
#7. Find Max Value Given {"Math": 85, "Science": 92, "English": 78}, find and print the subject with the highest marks.
#8. Word Frequency Counter Given a sentence like "apple banana apple orange banana apple", count how many times each word appears. Store the result in a dictionary.
#9. Merge Two Dictionaries Merge dict1 = {"a": 1, "b": 2} and dict2 = {"c": 3, "d": 4} into one dictionary and print it.
#10. Reverse a Dictionary Given {"a": 1, "b": 2, "c": 3}, create a new dictionary where keys and values are swapped → {1: "a", 2: "b", 3: "c"}.


#easy questions 

#1. Create & Access Create a dictionary with your name, age, and city. Print each value using its key.


person={"name":"Aditya","age":20,"city":"Delhi"}
print(person)

#2 questions -updated values 
print("updated values:")
person["price"]=15
person["item"]=10
print(person)

# 3. Add & Delete
#    Start with {"a": 1, "b": 2, "c": 3}
#    Add key "d": 4, then delete key "b". Print the result.

my_dict = {"a": 1, "b": 2, "c": 3}
print("Before:", my_dict)

# ADDING → just assign a new key
my_dict["d"] = 4
print("After adding 'd':", my_dict)

# DELETING → 3 ways:

# Way 1: del keyword (simply removes the key)
del my_dict["b"]
print("After deleting 'b' with del:", my_dict)

# Way 2: .pop() (removes AND returns the value)
removed_value = my_dict.pop("c")
print("Removed value:", removed_value)
print("After pop('c'):", my_dict)

# Way 3: .popitem() (removes the LAST item)
last_item = my_dict.popitem()
print("Last item removed:", last_item)
print("Final dictionary:", my_dict)

#way 4

my_dict.clear()
#4. Check if Key Exists Write a program that checks if "email" exists in a student dictionary. Print "Found" or "Not Found".
email={"email":"[EMAIL_ADDRESS]","name":"Aditya","age":20}
if "email" in email:
    print("Found")
else:
    print("Not Found")

#5. Count Items Create a dictionary with 5 fruits and their prices. Print how many items are in the dictionary using len().

fruits={"apple":10,"banana":20,"cherry":30,"orange":40,"kiwi":50}
print(len(fruits))

#medium questions
#6. Loop & Print Given a dictionary of 5 students and their marks, loop through and print: "Aditya scored 95 marks"

students = {
    "Aditya":95,
    "Rahul":88,
    "Priya":89,
    "Rohan":78,
    "Anjali":85
}
for name,marks in students.items():
    if marks>94:
        print(f"students:{name},marks:{marks}")
    else:
        print("no marks will  be awarded to the students ")


#7. Find Max Value Given {"Math": 85, "Science": 92, "English": 78}, find and print the subject with the highest marks.
students = {"Math": 85, "Science": 92, "English": 78,"Hindi":90,"Sanskrit":95,"Computer":98}
for name,marks in students.items():
    if marks>94:
        print(f"students:{name},marks:{marks}")
    else:
        print("no marks will  be awarded to the students ")

#max values
print(max(students.values()))


#8. Word Frequency Counter Given a sentence like "apple banana apple orange banana apple", count how many times each word appears. Store the result in a dictionary.
word={
    "apple":3,
    "banana":2,
    "orange":1
}
for word,count in word.items():
    if count>1:
        print(f"students:{word},count:{count}")
    else:
        print("no marks will  be awarded to the students ")

# in this question we have to count the frequency of each word in the sentence 
# as we have taken the words in the correct order.


#10. Reverse a Dictionary
#    {"a": 1, "b": 2, "c": 3} → {1: "a", 2: "b", 3: "c"}
#    We need to SWAP keys and values into a NEW dictionary

dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("\nOriginal:", dictionary)

# ❌ YOUR OLD CODE: This only PRINTS, does NOT create a new dict
# for key,value in dictionary.items():
#     print(value, key)

# ✅ METHOD 1: Using a for loop
reversed_dict = {}                          # Start with empty dict
for key, value in dictionary.items():       # Loop through each pair
    reversed_dict[value] = key              # value becomes key, key becomes value
print("Reversed (loop):", reversed_dict)

# ✅ METHOD 2: Dictionary comprehension (1 line!)
reversed_dict2 = {value: key for key, value in dictionary.items()}
print("Reversed (comprehension):", reversed_dict2)
