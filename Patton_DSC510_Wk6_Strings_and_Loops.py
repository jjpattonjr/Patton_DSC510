# DSC 510
# Week 6
# Programming Assignment
# Author: John Patton
# 20 Jan 2025
# Desc: User enters temps until sentinel value given; count, min, & max of temps output to user.


def main():
	temperatures = []	# Establishes empty list
	print("*** Program Start -- Type 'end' to cease entry ***")	# Informs user of sentinel input
	while True:	# while loop accepts entries until sentinel entered
		temp = input("Please enter temperature value:")
		if temp.lower() == "end":	# Evaluates string for sentinel value; if true, breaks from while loop
			break
		else:
			try:	# Attempts to convert string to float; catches non-numerical entries
				temp = float(temp)
				temperatures.append(temp)	# adds new temp to list
			except ValueError:	# Error catches non-numerical entries
				print("Please enter a valid number")	# Prints error message

	print("Total values entered: "+str(len(temperatures)))	# Determines & outputs list length

	# Evaluates to prevent min() & max() function errors
	if len(temperatures) == 0:	# if list length=0, then no min or max available
		print("No min or max value available")	# Informs user of no min/max value
	else:
		print("Lowest value: "+str(min(temperatures)))	# Output min value
		print("Highest value: "+str(max(temperatures)))	# Output max value
		print("*** End of Program ***")

if __name__ == "__main__":
	main()


# The purpose of this week’s assignment is to demonstrate the use of strings and loops in a Python program.
# This week we will create a program which works with lists. Your goal is to create a program which contains a list of
# temperatures. Your program will populate the list by prompting the user to input temperatures. Your program will
# determine the number of temperatures entered by the user and stored in the list, determine the largest temperature
# in the list, and the smallest temperature in the list.

# Your program must have the following elements:
# A header.
# Try blocks where appropriate to prevent unhandled exceptions.
# A Main method.
# An empty list called temperatures.
# Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
# Evaluate the temperatures in the temperatures list to determine the largest and smallest temperature.
# Print the largest temperature in a legible format.
# Print the smallest temperature in a legible format.
# Print a message that tells the user how many temperatures are in the list.
# Must have good coding practices.