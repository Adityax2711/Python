#functions in python i want to know 

#A function is a reusable block of code that performs a specific task. Instead of writing the same code again and again, you define it once inside a function and call it whenever needed.

#Why use functions?
#Reusability — Write once, use many times
#Organization — Break complex programs into smaller, manageable pieces
#Readability — Makes code easier to understand
#Debugging — Easier to find and fix error

def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function

#why we use def keyword 
#The def keyword in Python is used to define a function. Here's why it's important:

#1. It tells Python that you're creating a function
#2. It specifies the function name
#3. It indicates where the function code begins
#4. It allows you to define parameters (inputs) for the function
#5. It enables code organization and reusability


#function with parameters

def greet(name):
    print("Hello", name)

greet("Aditya")

#function with return value

def add(a, b):
    return a + b

print(add(1, 2))

#function with default parameters

def greet(name="Aditya"):
    print("Hello", name)

greet()
greet("Rahul")

#function with multiple parameters

def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))

#function with arbitrary parameters

def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))

#function with arbitrary keyword parameters

def greet(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

greet(name="Aditya", age=20, grade="A")

#function with lambda expression

add = lambda a, b: a + b
print(add(1, 2))

#function with lambda expression and multiple parameters

add = lambda a, b, c: a + b + c
print(add(1, 2, 3))

#function with lambda expression and arbitrary parameters

add = lambda *args: sum(args)
print(add(1, 2, 3, 4, 5))

#function with lambda expression and arbitrary keyword parameters

greet = lambda **kwargs: print(kwargs)
greet(name="Aditya", age=20, grade="A")

#function with lambda expression and arbitrary keyword parameters

greet = lambda **kwargs: print(kwargs)
greet(name="Aditya", age=20, grade="A")

#function with lambda expression and arbitrary keyword parameters

greet = lambda **kwargs: print(kwargs)
greet(name="Aditya", age=20, grade="A")

#function with lambda expression and arbitrary keyword parameters

greet = lambda **kwargs: print(kwargs)
greet(name="Aditya", age=20, grade="A")

#function with lambda expression and arbitrary keyword parameters

greet = lambda **kwargs: print(kwargs)
greet(name="Aditya", age=20, grade="A")


#def calcualte the sum

def calc_sum(a,b):
    sum = a + b 
    print("the sum of", a, "and", b, "is", sum)

calc_sum(1, 2)

def calc_sub(a,b):
    sub = a - b
    print("the sub of", a, "and", b, "is", sub)

calc_sub(1, 2)


def calc_mul(a,b):
    mul = a * b
    print("the mul of", a, "and", b, "is", mul)

calc_mul(1, 2)


def calc_div(a,b):
    div = a / b
    print("the div of", a, "and", b, "is", div)

calc_div(1, 2)

def calc_sum(a,b):
    return a + b

def calc_sub(a,b):
    return a - b

def calc_mul(a,b):
    return a * b

def calc_div(a,b):
    return a / b

print(calc_sum(55, 2))
print(calc_sub(145, 445))
print(calc_mul(123, 234))
print(calc_div(123, 234))

def calc_sum(a,b):
     return a + b

sum =  calc_sum(1,2)
print(sum)

#average of 3 number

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    return avg

avg = calc_avg(88,45,67)
print(avg)


#function  types 

#built in function and user definned function..
print("hello world")
print(len("hello world"))
print("hello world".upper())
print("hello world".lower())
print("hello world".title())
print("hello world".capitalize())
print("hello world".swapcase())
print("hello world".count("o"))
print("hello world".find("o"))
print("hello world".replace("o", "O"))
print("hello world".split())
print("hello world".join(["hello", "world"]))
print("hello world".strip())
print("hello world".lstrip())
print("hello world".rstrip())
print("hello world".startswith("hello"))
print("hello world".endswith("world"))
print("hello world".islower())
print("hello world".isupper())
print("hello world".istitle())
print("hello world".isspace())
print("hello world".isdigit())
print("hello world".isalpha())
print("hello world".isalnum())
print("hello world".isprintable())
print("hello world".isidentifier())
print("hello world".isdecimal())
print("hello world".isnumeric())

#user defined function

#Edited function.py

#Here are some great **practice questions on functions** for you to try! I'll add them to your file:

#Viewed function.py:200-206
#Edited function.py

#Here are **15 practice questions** added to your file, organized by difficulty:



#| **Easy** (Q1–Q5) | Max of two, Even/Odd, Area of circle, 
# elsius to Fahrenheit, Reverse string |
# Basic functions, parameters, return values |


#| **Medium** (Q6–Q10) | 
# Factorial, Prime check, Count vowels, Filter even numbers, Sum of digits |
# Loops inside functions, conditionals, lists |


#| **Hard** (Q11–Q15) | Fibonacci, Stats with `*args`, Recursion, Remove duplicates, Decorators 
#  `*args`, recursion, advanced concepts |
#Also fixed: removed `print("hello world".range(1,10))` — strings don't have a `.range()` method,
#  that would have caused an error.
