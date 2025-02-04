# DSC 510
# Week 5
# Programming Assignment Week 5
# Author: John Patton
# 13 Jan 2025
# Desc: Demonstrate while and for loops. Create program which uses a total of 2 functions and a main method.
#       Function 1 - perform_calculation: perform math calcs (+,-,*,/) given one input
#       Function 2 - calculate_average: ask user for num of values; ask for each value until count met; output avg.
#
from enum import nonmember

def perform_calculation(oper):
    # Desc: Receives mathematical operator (+, -, *, or /) and asks user for two numbers; returns resulting value.
    # Inputs: oper as string
    # Outputs: result as float
    # Variables: num1 and num2 as floats

    # Initializes num1 & num2 variables; catches non-numerical inputs passing through to operations
    num1 = 0
    num2 = 0
    # Attempts to capture two numbers from user
    try:
        num1 = float(input("Enter first of two numbers: "))
        num2 = float(input("Enter second of two numbers: "))
    except ValueError as e:
        print("\n*****\nInvalid operation\n User must provide two numbers \nError: ", e, "\n*****\n")

    # Attempts to perform selected operation
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        result = num1 / num2
    else:
        result = None
        print("\n*****\nInvalid operation \nUser must provide a valid operator: +, -, *, or /\n*****\n")

    return result


def calculate_average():
    # Desc:  ask user how many numbers they wish to input; use the number entered to control a "for" loop; within
    #   the loop, ask user for number value to calculate total and average. Return calc'd avg to main; print in main.
    # Inputs: none
    # Outputs: numOfNumbers as integer, mean as float

    # Initialize variable(s)
    total = 0
    numOfNumbers = 0
    mean = 0

    while numOfNumbers <= 0:
        try:
            # Request user input number of numbers to average
            numOfNumbers = int(input("How many numbers would you like to average?: "))
            if numOfNumbers <= 0:
                print("Please provide a positive integer")
        except ValueError:
            print("Please provide a positive integer")

    # For loop to collect numbers from user; While loop catches invalid entries
    while mean == 0:
        try:
            # For loop; prompts user for input & updates total
            for x in range(numOfNumbers):
                print("Entry", str(x+1), "of", str(numOfNumbers))
                total = total + float(input("Please enter number: "))   # user inputs number & updates total variable

            mean = total / numOfNumbers    # calculates mean average
            return numOfNumbers, mean   # Returns values to external program
        except ValueError:
            print("Please enter a valid number")


def main():
    # Welcome message
    print("Welcome to Patton DSC510, Week 5 Calc-u-la-tron\n")
    # Indefinite Loop; user selects (1) perform_calculation(), (2) calculate_average(), or (3) exits program
    while True:
        user_input1 = input("Please select from the following options:\n"  # User selects program
                            "(1) Perform Calc\n(2) Calculate Average\n(3) Exit Program\n")
        # Executes perform_calculation() function
        if user_input1 == "1":
            user_input2 = input("Please select from the following options:\n+, -, *, /\n")  # User selects operator
            result = perform_calculation(user_input2)
            print(f"The resulting value is: {result}\n")
        # Executes calculate_average() function
        elif user_input1 == "2":
            numOfNumbers, mean = calculate_average()
            if numOfNumbers == 1:
                print(f"The average of the one value is {mean}\n")
            else:
                print(f"The average of the {numOfNumbers} values is: {mean}\n")

        # Exits program
        elif user_input1 == "3":
            print("Thank you for using Patton DSC510 Calc-u-la-tron!")
            break

        # If user does not enter either 1, 2, or 3
        else:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
