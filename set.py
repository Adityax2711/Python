#Set Python mein ek unordered collection hai jisme unique elements hote hain — matlab duplicate values allowed nahi hain.
#Socho ek dabba (box) hai jisme tum cheezein daalte ho, lekin:
#1. Har cheez unique honi chahiye — agar ek apple daal diya, dobara apple nahi daal sakte (ya daaloge toh dikhega ek hi).


# Koi duplicate item nahi rakh sakte
# Koi fixed order nahi hota (index se access nahi kar sakte)
# Mutable hai — items add/remove kar sakte ho
# Bohot fast searching hoti hai

#Concept	Explanation
#Unordered	Set mein items ka koi order nahi hota. {1, 2, 3} aur {3, 1, 2} same hain
#Unique Elements	Duplicate automatically remove ho jaate hain
#Mutable	Tum items add/remove kar sakte ho, lekin set ke andar sirf immutable items rakh sakte ho (like int, string, tuple)
#No Indexing	my_set[0] kaam nahi karega — kyunki order hi nahi hai
#Hashing	Set internally hash table use karta hai, isliye searching O(1) time mein hoti hai — bohot fast!
#Math Operations	Union, Intersection, Difference — ye sab set pe directly kar sakte ho, bilkul math ki tarah


#How to Create a Set
#1. Using curly braces {}
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Using set() constructor
my_set = set([1, 2, 3, 4, 5])
print(my_set)

# 3. Empty set (IMPORTANT: {} creates an empty dictionary!)
empty_set = set()
print(empty_set)

# 4. Set with mixed data types
mixed_set = {1, "hello", 3.14, True}
print(mixed_set)

# 5. Set automatically removes duplicates
duplicate_set = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(duplicate_set)


#Adding and Removing Elements
my_set = {1, 2, 3}

# Add a single element
my_set.add(4)
print(my_set)

# Add multiple elements
my_set.update([5, 6, 7])
print(my_set)

# Remove an element (raises error if not found)
my_set.remove(3)
print(my_set)

# Remove an element (safe - no error if not found)
my_set.discard(8)
print(my_set)

# Remove and return an element
removed = my_set.pop()
print("Removed:", removed)
print("After pop:", my_set)

# Remove all elements
my_set.clear()
print(my_set)


#Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all elements from both sets)
print("Union:", set1.union(set2))
print("Union (using |):", set1 | set2)

# Intersection (common elements)
print("Intersection:", set1.intersection(set2))
print("Intersection (using &):", set1 & set2)

# Difference (elements in set1 but not in set2)
print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (using -):", set1 - set2)

# Symmetric Difference (elements in either set, but not both)
print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Symmetric Difference (using ^):", set1 ^ set2)

# Check subset
print("Is {1, 2} subset of set1?", {1, 2}.issubset(set1))

# Check superset
print("Is set1 superset of {1, 2}?", set1.issuperset({1, 2}))

# Check disjoint (no common elements)
print("Are set1 and {9, 10} disjoint?", set1.isdisjoint({9, 10}))


#Frozen Set
#Immutable version of a set (cannot be changed after creation)
#Can be used as dictionary keys or elements of another set

my_set = {1, 2, 3}
frozen_set = frozenset(my_set)
print(frozen_set)

# Can be used as dictionary key
dict_with_set = {frozen_set: "some value"}
print(dict_with_set)

# Cannot modify frozen set
# frozen_set.add(4)  # This will cause an error


#Set Comprehension
#Similar to list comprehension, but creates a set

# Create a set of squares
squares = {x**2 for x in range(1, 6)}
print(squares)

# Create a set of even numbers
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)

# Create a set from a string (unique characters)
word = "programming"
unique_chars = {char for char in word}
print(unique_chars)


#When to Use Sets
#Use sets when you need:
#1. To remove duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_items = set(my_list)
print(unique_items)

#2. To check for membership quickly (O(1) time)
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Very fast!

#3. To perform mathematical set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

#4. To find unique elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1) & set(list2)
print(common_elements)


#Common Pitfalls
#1. Creating an empty set
# WRONG: empty_set = {}
# RIGHT: empty_set = set()

#2. Adding mutable items to a set
# my_set = {1, 2, [3, 4]}  # This will cause TypeError!
# Sets can only contain immutable items (numbers, strings, tuples)

#3. Forgetting that sets are unordered
my_set = {1, 2, 3}
print(my_set)  # Output order may vary!


#Summary
#Feature	Description
#Syntax	{element1, element2, ...} or set()
#Unordered	No fixed order
#Duplicates	Not allowed
#Mutable	Can add/remove elements
#Indexing	Not supported
#Membership	Fast (O(1))
#Operations	Union, Intersection, Difference, etc.
#Frozen Set	Immutable version, can be used as dictionary keys