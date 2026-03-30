#list 

# A list is mutable. In programmer-speak, that means you can change it after you create it. You can add, remove, or swap items at will.
# Syntax: Defined using square brackets [].
# Vibe: It’s a flexible container. Need to keep track of users logging into a chatroom? Use a list. People leave and join all the ti
# When to use Lists:
# Dynamic Data: When you don’t know how many items you’ll have (e.g., results from a database query).
# 
# Sorting/Ordering: If you need to frequently sort, reverse, or shuffle your data.
# 
# Homogeneous Data: Usually, we use lists for a collection of the same types of things (e.g., a list of Price objects).

lst=[]
print(type(lst))

mixed_list=[1,"hello",3.14,True]
print(mixed_list)
print(type(mixed_list))

#list are mutable 
#Accesing the elemts in the list 


fruits=["apple ","banana","cherry","orange","kiwi","mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
#if we want to do indexing tin the python we will do this 

print(fruits[0:3])

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])
print(fruits[-6])


#list methods

#add the elements in the list 

fruits.append("grapes")
print(fruits)

#insert the elements in the list 

fruits.insert(2,"pineapple")
print(fruits)

#remove the elements from the list 

fruits.remove("banana")
print(fruits)

#pop the elements from the list 

fruits.pop()
print(fruits)

#clear the list 

fruits.clear()
print(fruits)

#copy the list 

fruits.copy()
print(fruits)




#sort the list 

fruits.sort()
print(fruits)

#reverse the list 

fruits.reverse()
print(fruits)

#length of the list 

print(len(fruits))

#sum of the list 

print(sum(fruits))

#min of the list 

print(min(fruits))

#max of the list 

print(max(fruits))

#modify 
fruits[0]="orange"
print(fruits)

#delete 
del fruits[0]
print(fruits)

#slicing the numbeers

numbers = [1,2,3,4,5,6,7]
print(numbers[2:5])
print(numbers[:5])
print(numbers[2:])
print(numbers[2:5:2])
print(numbers[2:5:-1])
print(numbers[::3])


#list comprehension 

numbers = [1,2,3,4,5,6,7]
new_list = [i*2 for i in numbers]
print(new_list)

lst=[]
for x in range(10):
    lst.append(x**2)
print(lst)

#list comprehension with condition 

numbers = [1,2,3,4,5,6,7]
new_list = [i*2 for i in numbers if i%2==0]
print(new_list)


#list comprehension with nested loop 

numbers = [1,2,3,4,5,6,7]
new_list = [i*j for i in numbers for j in numbers]
print(new_list)


#list comprehension with nested loop and condition 

numbers = [1,2,3,4,5,6,7]
new_list = [i*j for i in numbers for j in numbers if i%2==0 and j%2==0]
print(new_list)

#iteration with the index 

for index,number in enumerate(numbers):
    print(index,number)

#basic list comprehenion 
squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)


# list the comprehnison with condition  nested comprehnsion 

list1=[1,2,3,4,5,6,7,8,9]
list2=['a','b','c','d']
pair=[ (i,j) for i  in list1 for j in list2]
print(pair)


#lis comprehsion with thee function calls
words = ["hello","world","python","loops","Dictionary"]
lengths = [len(word) for word in words]
print(lengths)


#list comprehnsion with thee function calls
words = ["hello","world","python","loops","Dictionary"]
lengths = [len(word) for word in words]
print(lengths)
