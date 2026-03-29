#build calculator
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return " Cannot divide by zero"
    return x / y
def percent(x,y):
    return x%y

def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def cot(x):
    return math.cot(math.radians(x))
def sec(x):
    return math.cot(math.radians(x))
def cosec(x):
    return math.cosec(math.radians(x))
def log(x):
    return math.log(x)
def root(x):
    return math.sqrt(x)

print(" Simple Calculator")
print(" Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. percent")
print("6. sin")
print("7. cos")
print("8. tan")
print("9. cot")
print("10. sec")
print("11. cosec")
print("12. log")
print("13. root")

option= input("Enter option (1/2/3/4/5/6/7/8/9/10/11/12): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if option == '1':
    print(f"Result: {add(num1, num2)}")

elif option == '2':
    print(f"Result: {subtract(num1, num2)}")

elif option == '3':
    print(f"Result: {multiply(num1, num2)}")

elif option == '4':
    print(f"Result: {divide(num1, num2)}")

elif option=="5":
    print(f"result:{percent(num1,num2)}")

elif option=="6":
    angle=float(input("enter the angle value in degrees:"))
    print(f"result:{sin(angle)}")

elif option=="7":
    angle=float(input("enter the angle value in degree:"))
    print(f"result:{cos(angle)}")

elif option=="8":
    angle=float(input("enter the angle value in degree:"))
    print(f"result:{tan(angle)}")

elif option=="9":
    angle=float(input("enter the angle value in degree:"))
    print(f"result:{cot(angle)}")

elif option=="10":
    angle=float(input("enter the angle value in degree:"))
    print(f"result:{sec(angle)}")

elif option=="11":
    angle=float(input("enter the angle value in degree:"))
    print(f"result:{cosec(angle)}")

elif option=="12":
    x=float(input("enter number:"))
    print(f"result:{root(x)}")

else:
    print(" Invalid input")
