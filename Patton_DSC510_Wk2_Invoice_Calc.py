# DSC 510
# Week 2
# Programming Assignment Week 2
# Author: John Patton
# 28 Nov 2024
# Desc: Receive customer input for company name and distance of fiber optic cable to be installed;
#       repeat back company name, distance, & total cost in invoice.

# Import datetime module for date/time stamp & locale module to format currency
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Welcome message
print("Welcome to Patton DSC510, Week 2 Invoice Calc")
# Request company name input
coName = input("Please provide company name:\n")
# Request install distance (ft) input
distFt = float(input("Please provide distance of fiber optic to be installed (in feet):\n"))
# establish USD cost per distance in feet
costPerFt = float(0.95)
# calc estimated cost
estCost = float(costPerFt*distFt)

# Print invoice
print("*************************************************************************************************************\n")
print("*** Invoice for company: "+coName+" ***")
# Output distance requested using format method
print("Distance (ft): "+str("{:.2f}".format(distFt))+"")
# Output estimated cost using locale to format currency
print("Install Cost: "+str(locale.currency(estCost))+"\n")
# Output current time with date/time formatted
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print("*************************************************************************************************************")

# Change#: 0
# Change(s) Made: N/A
# Date of Change: N/A
# Author:
# Change Approved by:
# Date Moved to Production:
