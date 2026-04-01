#Conclusion
#Loops are powerful constructs in Python that allow you to execute blocks of code multiple times. By understanding and using for and while loops,
#  along with loop control statements like break, continue, and pass, you can handle a wide range of programming tasks efficiently. 
# More examples and applications will be explored as you continue learning.

#WAP FOR THE LOOP 
total=0
for i in range(1,101):
    total+=i
print(total)

#WAP WHILE LOOP 
total=0
count=1
while count<=100:
    total+=count
    count+=1
print(total)


# wap for the loop 
# wap while loop 
# wap for the loop with break 
# wap for the loop with continue 
# wap for the loop with pass 

total=0
for i in range(1,101):
    total+=i
print(total)


# wap for the loop with break 
total=0
for i in range(1,101):
    total+=i
    if total>=500:
        break
print(total)

# wap for the loop with continue 
total=0
for i in range(1,101):
    total+=i
    if total>=500:
        continue
print(total)

# wap for the loop with pass 
total=0
for i in range(1,101):
    total+=i
    if total>=500:
        pass
print(total)


# Easy: Foundations of Iteration
# Goal: Master the syntax of for and while loops and basic accumulators.
# - The Sum of Evens: Write a program that calculates the sum of all even numbers between 1 and 100 (inclusive).
# - Character Counter: Given a string (e.g., "Python loops are fun"), use a loop to count how many vowels are present.
# - Factorial Finder: Ask the user for a number and calculate its factorial (n!) using a while loop.
# - The Countdown: Create a loop that prints a countdown from 10 to 1 and then prints "Blast off!"
# - Multiplication Table: Print the multiplication table for the number 7 (from 1 to 12).
# - List Doubler: Given a list of integers, create a new list where every value is doubled using a for loop.
# - Simple Pattern: Print a right-angled triangle of asterisks with a height of 5.
#   *
#   **
#   ***
#   ****
#   *****
#
#  Medium: Nested Loops & Data Manipulation
# Goal: Handling multi-dimensional logic and combining loops with conditional filtering.
# - Prime Number Checker: Write a loop to determine if a given number n is prime.
# - Unique Element Filter: Given a list with duplicate items, use a loop to create a new list containing only the unique elements (without using the set() constructor).
# - Number Pyramid: Use nested loops to print a pyramid of numbers like this:
#   1
#   2 2
#   3 3 3
#   4 4 4 4
# - List Flattening: Given a list of lists (e.g., [[1, 2], [3, 4], [5]]), use nested loops to "flatten" it into a single list: [1, 2, 3, 4, 5].
# - The Fibonacci Sequence: Generate and print the first 15 numbers of the Fibonacci sequence using a loop.
# - Palindrome Tester: Use a loop to check if a string (ignoring case) reads the same forwards and backwards.
# - Common Elements: Given two lists, use a loop to find and print the elements that appear in both.
#
#  Hard: Algorithmic Thinking & Efficiency
# Goal: Solving complex problems that require state management and optimized nested logic.
# - Bubble Sort Implementation: Sort a list of numbers in ascending order using the Bubble Sort algorithm (using nested loops and swapping).
# - Pascal's Triangle: Given an integer n, generate the first n rows of Pascal's Triangle using nested loops.
# - Matrix Multiplication: Given two 3x3 matrices (represented as lists of lists), calculate their product using triple-nested loops.
# - The "Longest Substring": Write a loop to find the length of the longest substring without repeating characters in a given string.
# - Caesar Cipher: Create a program that encrypts a sentence by shifting each letter by a fixed number k (e.g., if k=3, 'A' becomes 'D'). Handle both uppercase and lowercase.
# - Sudoku Row/Column Validator: Given a 9x9 grid (list of lists), write a loop-based logic to verify if every row and every column contains the digits 1 through 9 without repeats.


# Easy: Foundations of Iteration
# Goal: Master the syntax of for and while loops and basic accumulators.
# - The Sum of Evens: Write a program that calculates the sum of all even numbers between 1 and 1000 (inclusive).

total_sum = 0
for i in range(1, 100):
    if i % 2 == 0:
        total_sum += i
print("even no:", total_sum)

#use pin put takin the next code 
user_limit = int(input("Enter the maximum number to check: "))
total_sum = 0
for i in range(1, user_limit + 1): 
    if i % 2 == 0:
        total_sum += i
print("even no:", total_sum)


# - Character Counter: Given a string (e.g., "Python loops are fun"), use a loop to count how many vowels are present.
user_string=input("enter the string:")
total_vowels=0
for i in user_string:
    if i in "aeiouAEIOU":
        total_vowels+=1
print("vowels:",total_vowels)


# - Factorial Finder: Ask the user for a number and calculate its factorial (n!) using a while loop.

user_number=int(input(" enter the number :"))
factorial=1
count=1
while count<=user_number:
    factorial=factorial*count
    count+=1
print("factorial:",factorial)  

# - The Countdown: Create a loop that prints a countdown from 10 to 1 and then prints "Blast off!"
user_number=int(input("enter the numbeer from he 0 to the 12:"))
for i in range(user_number,0,-1):
    print(i)
print("Blast off!")

# - Multiplication Table: Print the multiplication table for the number 7 (from 1 to 12).
user_table=int(input("entter the number:"))
for i in range(1,13):
    print(user_table,"x",i,"=",user_table*i)

# - List Doubler: Given a list of integers, create a new list where every value is doubled using a for loop.
user_list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in user_list:
    new_list.append(i*2)
print(new_list)
#append is use when we have to add the value in the list 


# THE UNIVERSAL LOOP PATTERN (The Accumulator Pattern)
# Almost every loop problem follows this exact 4-step sequence:
#
# 1. INITIALIZE / SETUP (Before the loop):
#    Set up starting variables like `total_sum=0`, `count=1`, or `new_list=[]`.
#
# 2. THE LOOP (Iterate):
#    Start `for` or `while` loop to go through elements. (e.g., `for i in range():`)
#
# 3. CONDITION & UPDATE (Inside the loop):
#    Check conditions (optional) and modify your initialized variables. 
#    (e.g., `total_sum += i`, `new_list.append(i * 2)`, `factorial *= count`)
#
# 4. FINAL RESULT (After the loop):
#    Print or return the final calculated value outside the loop block. 
#    If printed inside, it prints over and over.
# 
# - Simple Pattern: Print a right-angled triangle of asterisks with a height of 5.
#   *
#   **
#   ***
#   ****
#   *****

user_pattern=int(input("enter the number:"))
for i in range(1,user_pattern+1):
    print("*"*i)

# - Prime Number Checker: Write a loop to determine if a given number n is prime.
user_number=int(input("enterthe number:"))
for i  in range (2,user_number):
    if user_number%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break

# - Unique Element Filter: Given a list with duplicate items, 
# use a loop to create a new list containing only the unique elements 
# (without using the set() constructor).

user_list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in user_list:
    if i not in new_list:
        new_list.append(i)
        
        break
    else:
        print("duplicate")
        break
print(new_list)

# - Number Pyramid: Use nested loops to print a pyramid of numbers like this:
#   1
#   2 2
#   3 3 3
#   4 4 4 4

user_list=[1,2,3,4,]
new_list=[]
for i in range(1,4):
    for j in range(i):
        print(i,end=" ")
    print()



