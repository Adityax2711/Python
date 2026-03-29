name = "Krish"
Name = "Nick"
print(name)
print(Name)


"""
This is a multi-line comment.
Welcome to the Python course.
"""


age = 32
if age > 30:
    print(age)
print(age)


#basic prblms
total = 1 + 2 + 3 + 4 + 5 + 6 + 7 + \
    8 + 9 + 10
print(total)

age = 32
name = "Krish"
print(type(age))
print(type(name))

variable = 10
print(type(variable))
variable = "Krish"
print(type(variable))

age = 32
if age > 30:
    print(age)  # fixed indentation error
b = 0  # define b to avoid NameError
a = b  # now works

if True:
    print("This is my correct indentation")
    if False:
        print("this will not print")
    print("This will print")
print("Outside the if block")

x=5; y=10;z=x*y
print(x)
print(z)

message = "Hello, World!"
print(message)

age = 32
height = 6.1
name = 'Krish'
is_student = True
print('Age:', age)
print('Height:', height)
print('Name:', name)
first_name = 'Krish'
last_name = 'Nick'

print(type(age))  # <class 'int'>
print(type(name))  # <class 'str'>
#typechecking

#type checking nad conversion
age = 25
print(type(age))  # <class 'int'>
age_str = str(age)
print(age_str)  # '25'
print(type(age_str))  # <class 'str'>

#claas define how 
var=10
print(type(var))  # <class 'int'>
var=str(var)
print(type(var))  # <class 'str'>


sir= False
print(type(sir))
sir= bool(sir)
print(type(sir))  # <class 'bool'>

pi=3.14
print(type(pi))  # <class 'float'>
pi= float(pi)
print(type(pi))  # <class 'float'>

#
a = 10
b = 15
add_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b
floor_div_result = a // b
modulus_result = a % b
exponential_result = a ** b
print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(floor_div_result)
print(modulus_result)
print(exponential_result)

#comparison operators

str1 = "Crush"
str2 = "Crush"
print(str1 == str2)
str3 = "crush"
print(str1 == str3)
print(str1 != str3)

