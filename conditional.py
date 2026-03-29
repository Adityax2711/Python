def main():
    age = 20
    if age >= 20:
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")

    try:
        number = int(input("Enter the number: "))
    except ValueError:
        print("Invalid input; please enter an integer.")
    else:
        if number > 0:
            print("The number is positive.")
            if number % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")
        elif number == 0:
            print("The number is zero.")
        else:
            print("The number is negative.")

    try:
        marks = int(input("Enter the marks: "))
    except ValueError:
        print("Invalid input; please enter numeric marks.")
    else:
        if marks >= 90:
            print("Grade A")
        elif marks >= 80:
            print("Grade B")
        elif marks >= 70:
            print("Grade C")
        elif marks >= 60:
            print("Grade D")
        else:
            print("Grade F")

if __name__ == "__main__":
    main()

number = int(input("Enter the number: "))
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero or negative.")


year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")

#questions on conditionaal statment 

#make the currency converter 
Currency=int(input("Enter the amount in INR: "))
target_currency=input("Enter the target currency (EUR, USD, Yen,Singapore dollar,kuwait Dollar,Dhereum,Taka,pound,Afghani,AUD,kiwi,): ")
if target_currency=="USD":
    converted_amount=Currency*83.0
    print(f"Amount in USD: {converted_amount}")

elif target_currency=="EUR":
    converted_amount=Currency*106.86
    print(f"Amount in EUR: {converted_amount}")

elif target_currency=="Yen":
    converted_amount=Currency*24.67
    print(f"Amount in Yen: {converted_amount}")

elif target_currency=="Singapore dollar":
    converted_amount=Currency*71.11
    print(f"Amount in Singapore dollar: {converted_amount}")

elif target_currency=="kuwait Dollar":
    converted_amount=Currency*237.33
    print(f"Amount in kuwait Dollar: {converted_amount}")

elif target_currency=="Dhereum":
    converted_amount=Currency*24.67
    print(f"Amount in Dhereum: {converted_amount}")

elif target_currency=="Taka":
    converted_amount=Currency*0.06
    print(f"Amount in Taka: {converted_amount}")

elif target_currency=="pound":
    converted_amount=Currency*123.99
    print(f"Amount in pound: {converted_amount}")

elif target_currency=="Afghani":
    converted_amount=Currency*0.91
    print(f"Amount in Afghani: {converted_amount}")

elif target_currency=="AUD":
    converted_amount=Currency*54.0
    print(f"Amount in AUD: {converted_amount}")

elif target_currency=="kiwi":
    converted_amount=Currency*50.0
    print(f"Amount in kiwi: {converted_amount}")

else:
    print("Invalid target currency.plz enter the correct currency")

    #universal template for the conditional statements in the python 

