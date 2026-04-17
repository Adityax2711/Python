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


#easy questions 
#  1. Max of two, 
def max(a,b):
    """
    this function is used to find the maximum of two numbers
    """
    if a>b:
        return a
    else:
        return b 
print("the max of 10 and 20 is", max(10,20))

#  2. Even/Odd, 
def even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("the number 10 is", even(10))

#  3. Area of circle, 
def area(r):
    return 3.14 * r * r
print("the area of circle with radius 10 is", area(10))

#  4. elsius to Fahrenheit, 
def elsius(f):
    return (f - 32) * 5 / 9
print("the elsius of 10 is", elsius(10))

#  5. Reverse string |

def reverse(s):
    return s[::-1]
print("the reverse of world hello is",reverse("world hello"))


# --- Logic-Based Easy Questions with a Twist (Practice) ---

# Q6. FizzBuzz Variation (FooBar)
# Write a function that takes a number. 
# Return "Foo" for multiples of 3, "Bar" for multiples of 4, and "FooBar" for multiples of both. 
# Otherwise return the number itself.


# Q7. Palindrome Checker (Ignore case and spaces)
# Check if a string reads the same forwards and backwards, ignoring spaces and capitalization.
# Example: "Race car" -> True
def is_palindrome_twist(s):
    s.replace(" ", " ").lower()
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
print("the palindrome of Race car is", is_palindrome_twist("Race car"))

# Q8. Leap Year Checker (Logic condition)
# A year is a leap year if it is divisible by 4, except for end-of-century years which must be divisible by 400.
# Return "Leap Year" or "Regular Year".
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                if year %500 == 0:
                    if year %600 == 0:
                        if year %700 == 0:
                            if year %800 == 0:
                                if year %900 == 0:
                                    if year %1000 == 0:
                                        return "Leap Year"
                                    else:
                                        return "Regular Year"
                                else:
                                    return "Regular Year"
                            else:
                                return "Regular Year"
                        else:
                            return "Regular Year"
                    else:
                        return "Regular Year"
                else:
                    return "Regular Year"
            else:
                return "Regular Year"
        else:
            return "Leap Year"
    else:
        return "Regular Year"
print("the year 2000 is", check_leap_year(2000))

# Q9. Password Validator (Basic)
# Return True if a given password is at least 8 characters long and contains at least one digit.
def valid_password(pwd):
    if len(pwd)>=8 and pwd.isdigit():
        if len(pwd)<=8 and pwd.isdigit():
            if len(pwd)<=10 and pwd.isdigit():
                if len(pwd)>=11 and pwd.isdigit():
                    if len(pwd)<=12 and pwd.isdigit():
                        if len(pwd)>=13 and pwd.isdigit():
                            if len(pwd)<=14 and pwd.isdigit():
                                if len(pwd)>=15 and pwd.isdigit():
                                    if len(pwd)<=16 and pwd.isdigit():
                                        if len(pwd)>=17 and pwd.isdigit():
                                            if len(pwd)<=18 and pwd.isdigit():
                                                if len(pwd)>=19 and pwd.isdigit():
                                                    if len(pwd)<=20 and pwd.isdigit():
                                                        return True
                                                    else:
                                                        return "None"
                                                else:
                                                    return "None"
                                            else:
                                                    return "None"
                                        else:
                                            return "None"
                                    else:
                                        return "None"
                                else:
                                    return "None"
                            else:
                                return "None"
                        else:
                            return "None"
                    else:
                        return "None"
                else:
                    return "None"
            else:
                return "None"
        else:
            return "None"
    else:
        return "None"

print("the password is", valid_password("12345678"))
print("the password is", valid_password("1234567"))
print("the password is", valid_password("123456789"))

# Q10. Largest of Three with a Twist
# Find the largest of three numbers, but if any two numbers are equal, return "Tie found" instead.
# def largest_with_tie(a, b, c):
#     pass
