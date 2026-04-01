#tupple in python 
# Syntax: Defined using parentheses ().
# Vibe: It’s an immutable ordered sequence. Once created, you cannot change, add, or remove items.
# When to use Tuples:
# Fixed Data: When you have a collection of items that should not change (e.g., coordinates (x, y), RGB color values).
# Dictionary Keys: Since tuples are immutable, they can be used as keys in a dictionary (lists cannot).
# Performance: Slightly faster and more memory-efficient than lists.
#hence in the tupple are immutable we cannot change anythiinn in tupple also in the tupple .
#they are the once you create a tuple, you cannot change, add, or remove items from it.
#tuple are immutable    
#questions are in tupple 




my_tupple=("apple ","banana","cherry","orange","kiwi","mango")
print(my_tupple)


tupple=("example",)
print(tupple)
print(type(tupple))

#accessing the elements in the tupple 

print(my_tupple[0])
print(my_tupple[1])
print(my_tupple[2])
print(my_tupple[3])
print(my_tupple[4])
print(my_tupple[5])

#slicing the tupple 

print(my_tupple[0:3])
print(my_tupple[-1])
print(my_tupple[-2])
print(my_tupple[-3])
print(my_tupple[-4])
print(my_tupple[-5])
print(my_tupple[-6])




#length of the tupple 

print(len(my_tupple))




#min of the tupple 

print(min(my_tupple))

#max of the tupple 

print(max(my_tupple))

#tuple comprehension 

tupple = (i*2 for i in range(10))
print(tupple)

#tuple comprehension with condition 

tupple = (i*2 for i in range(10) if i%2==0)
print(tupple)

#tuple comprehension with nested loop 

tupple = (i*j for i in range(10) for j in range(10))
print(tupple)

#tuple comprehension with nested loop and condition 

tupple = (i*j for i in range(10) for j in range(10) if i%2==0 and j%2==0)
print(tupple)

#iteration with the index 

for index,number in enumerate(my_tupple):
    print(index,number)

#basic tuple comprehension 

squares=()
for x in range(10):
    squares.append(x**2)
print(squares)


# tuple the comprehnsion with condition  nested comprehnsion 

tuple1=[1,2,3,4,5,6,7,8,9]
tuple2=['a','b','c','d']
pair=[ (i,j) for i  in tuple1 for j in tuple2]
print(pair)


#tuple comprehnsion with thee function calls
words = ["hello","world","python","loops","Dictionary"]
tuples = [len(word) for word in words]
print(tuples)


#tuple comprehnsion with thee function calls
words = ["hello","world","python","loops","Dictionary"]
tuples = [len(word) for word in words]
print(tuples)

