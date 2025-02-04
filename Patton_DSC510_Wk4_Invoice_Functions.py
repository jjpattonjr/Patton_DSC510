# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: John Patton
# 22 Dec 2024
# Desc: Receive customer input for company name and distance of fiber optic cable to be installed;
#       repeat back company name, distance, & total cost in invoice. Implement if & try blocks;
#       Implement and call functions.

import datetime
import locale


def total_cost(dist, cost):  # Function to calculate estimated total cost; imports distance & cost
    estCost = dist * cost
    return estCost


def main():
    # Import datetime module for date/time stamp & locale module to format currency (Standard, ext/3rd, Local)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Welcome message
    print("Welcome to Patton DSC510, Week 4 Invoice Calc\n"
          "Now with more conditionals and functions!\n")
    # Request company name input
    coName = input("Please provide company name:\n")
    # Request install distance (ft) input
    distFt = input("Please provide distance of fiber optic to be installed (in feet):\n")

    # Evaluate whether distFt variable string is convertable to float; otherwise request user input valid number
    while distFt != type(float):  #
        try:
            # Attempt to convert distFt variable into floating point number
            distFt = float(distFt)
            # Breakout of while loop after successfully converting distFt to float
            break
        except ValueError as e:  # If converting distFt to float fails (results in ValueError)
            # Request user input a numeric value for distFt
            print("Provided value not a number. \n Error:  ", e, ".")
            distFt = input("Please provide distance of fiber optic to be installed (in feet):\n")

    # Establish USD cost per distance in Ft; pricing length dependent
    if distFt <= 100:  # <=100 Ft, then $0.95/Ft
        costPerFt = 0.95
    elif distFt <= 250:  # >100 Ft & <=250 Ft, then $0.85/Ft
        costPerFt = 0.85
    elif distFt <= 500:  # >250 Ft & <=500 Ft, then $0.75/Ft
        costPerFt = 0.75
    else:
        costPerFt = 0.55  # >500 Ft, then $0.55/Ft (bulk)

    # Call total_cost function to calc estimated total cost
    estCost = total_cost(distFt, costPerFt)

    # Print invoice
    print("****************************************************************************************************\n")
    print("*** Invoice for company: " + coName + " ***")
    # Output distance requested using format method
    print("Distance (ft): " + str("{:.2f}".format(distFt)) + "")
    # Output estimated cost using locale to format currency
    print("Cost per foot: " + str(locale.currency(costPerFt)) + "")
    print("Install Cost: " + str(locale.currency(estCost)) + "\n")
    # Output current time with date/time formatted
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print("****************************************************************************************************\n")


if __name__ == "__main__":
    main()


# Change#: 0
# Change(s) Made: N/A
# Date of Change: N/A
# Author:
# Change Approved by:
# Date Moved to Production:
