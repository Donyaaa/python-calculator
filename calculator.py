# =====> CALCULATOR <=====
import math

print("----------------------------------------------------")
print("|                                                   |")
print("|                    CALCULATOR                     |")
print("|                                                   |")
print("----------------------------------------------------")

def get_float (message):
    while True:
        try:
          return float(input(message))
        except ValueError:
           print("Invalid Input! Please enter a number")

def get_int (message):
    while True:
        try:
          return int(input(message))
        except ValueError:
           print("Invalid Input! Please enter an integer")

while True:

    op = input("Enter Operator( +,-,*,/,%%,**,//,%,√,!,avg,log,max,min,abs): ").lower()

    # =========================================================================
    if op == "√":
        num1 = get_float("Enter a Number: ")
        if num1 < 0:
            print("Error: Square root of a negative number")
        else:
            result = math.sqrt(num1)
            print(f"Square root: {result}")
    # =========================================================================
    elif op == "**":
        num1 = get_float("Enter Base: ")
        num2 = get_float("Enter Exponent: ")
        result = num1 ** num2
        print(f"Exponentiation: {result}")
    # =========================================================================
    elif op == "!":
        num1 = get_int("Enter a Number: ")
        if num1 < 0:
            print("Error: Factorial is not defined for negative numbers")
        else:
            result = math.factorial(num1)
            print(f"Factorial: {result}")
    # =========================================================================
    elif op == "abs":
        num1 = get_float("Enter a Number: ")
        result = abs(num1)
        print(f"Absolute Value: {result}")
    # =========================================================================
    elif op == "%":
        num1 = get_float("Enter Percentage: ")
        num2 = get_float("Enter Number: ")
        result = (num1 / 100) * num2
        print(f"Percentage: {result}")
    # =========================================================================
    elif op == "avg":
        num1 = get_int("How many numbers do you want to average?")
        total = 0
        if num1 > 0:
            for i in range(num1):
                num2 = get_float(f"Enter Number {i + 1}:")
                total += num2
            result = total / num1
            print(f"Average: {result}")
        else:
            print("Error:At least one number is required")
    # =========================================================================
    elif op == "log":
        num1 = get_float("Enter Base: ")
        num2 = get_float("Enter Number: ")
        if num1 > 0 and num1 != 1 and num2 > 0:
            result = math.log(num2, num1)
            print(f"Logarithm: {result}")
        else:
            print("Error: Invalid Logarithm!!!")
    # =========================================================================
    elif op == "max":
        arr = get_int("How many numbers do you want to max?")
        Max_num = []
        if arr > 0:
            for i in range(arr):
                num2 = get_float(f"Enter Number {i + 1}:")
                Max_num.append(num2)
            print(f"Maximum:  {max(Max_num)}")
        else:
            print("Error: At least one number is required")
    # =========================================================================
    elif op == "min":
        arr = get_int("How many numbers do you want to min?")
        Min_num = []
        if arr > 0:
            for i in range(arr):
                num2 = get_float(f"Enter Number {i + 1}:")
                Min_num.append(num2)
            print(f"Minimum: {min(Min_num)}")
        else:
            print("Error: At least one number is required")
    else:
        num1 = get_float("Enter First Number: ")
        num2 = get_float("Enter Second Number: ")
    # =========================================================================

        if op == "+":
            result = num1 + num2
            print(f"Sum: {result}")


        elif op == "-":
            result = num1 - num2
            print(f"Difference: {result}")


        elif op == "*":
            result = num1 * num2
            print(f"Multiplication: {result}")


        # return float
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"Division: {result}")
            else:
                print("Undefined: Division by zero!")


        elif op == "%%":
            if num2 != 0:
                result = num1 % num2
                print(f"Modulo:  {result}")
            else:
                print("Undefined: Division by zero!")

        # return int
        elif op == "//":
            if num2 != 0:
                result = num1 // num2
                print(f"Floor Division:  {result}")
            else:
                print("Undefined: Division by zero!")

        else:
            print("Invalid Operator")
    # =========================================================================
    again = input("Do you want to continue? (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break

