# DSC 510
# Week 9
# Programming Assignment
# Author: John Patton
# 10 Feb 2025
# Desc: Demonstrate ability to read/process a file & write to new text file.
#
# Wk8: Demonstrate creating a dictionary by processing a file to parse the content and store it in a dictionary.
# Create a program which performs 3 ops to process a file.
# - It will open and process a txt file (gettysburg.txt) to create a dictionary of key value pairs.
# - The key will be the unique word and the value will be the number of occurrences of that word in the file.
# - To determine the unique words your program must remove punctuation from the words, convert the words to a common
# 	case, and remove any whitespace.
import string

def add_word(word, dictionary):
	# Desc: Add each word to dictionary; parameters are word & dictionary; no return value.
	# Input: word - string; reduced to all lowercase by call
	# 		 dictionary - active dictionary of word:Count pairs.
	# Output: None
	# Locals: None

	# Determines whether word (key) is in dictionary
	if word in dictionary:
		dictionary[word] += 1  # +1 to value for word (key)
	else:  # Else, if word (key) not in dictionary, add word to dictionary w/1 count
		dictionary[word] = 1


def process_line(line, dictionary):
	# Desc: Strip off characters/punctuation, split out words into list; parameters are line & dictionary
	#		Function will call add_word with each processed word to increment word count; no return value.
	# Input: line - string striped from provided text
	# 		 dictionary - active dictionary of word:Count pairs.
	# Output: None
	# Locals: translator - string; enables removal of punctuation in maketrans()
	#		  line_list - string; enables removal of punctuation in translate()

	# Make translation table that maps all punctuation character to None.
	translator = str.maketrans('', '', string.punctuation)

	# Applies translation table to the input string; splits string into space-parsed list without punctuation
	line_list = line.translate(translator).split()

	# Cycles through words in list and calls add_word
	for word in line_list:
		add_word(word.lower(), dictionary)  # Calls add_word & removes caps

def process_file(dictionary, filename):
	# Desc: Print to file function; no return value. Use Str formatting to print tabular-format output.
	# Input: dictionary - active dictionary of word:Count pairs.
	#		 filename - name of output file to be appended
	# Output: None

	# Sort dictionary by count (value); assign sorted dictionary to new local variable
	sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

	# Append to file
	try:
		with open(filename, 'a') as fileHandleWrite:  # Open file as append
			# Write header
			fileHandleWrite.write("\n")
			fileHandleWrite.write(f"{"Word":<12}Count")
			fileHandleWrite.write("\n")
			fileHandleWrite.write("*****************")
			fileHandleWrite.write("\n")

			# Write sorted dictionary word & count pairs
			for word in sorted_dictionary:  # Cycles through all word (keys) in dictionary until complete
				fileHandleWrite.write(f"{word:<12} {dictionary[word]}")  # Prints each word (key) with count (value)
				fileHandleWrite.write("\n")

	except FileNotFoundError as e:  # Catches error if file not in same dir as .py file
		print("File not found", str(e))


def pretty_print(dictionary):
	# Desc: Separate Print function; no return value. Use Str formatting to print output in tabular format.
	# Input: dictionary - active dictionary of word:Count pairs.
	# Output: None
	# Locals: sorted_dictionary - dictionary; required to sort key-value pairs by values

	# Sort dictionary by count (value); assign sorted dictionary to new local variable
	sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

	# Print table header
	print(f"{"Word":<12}Count")
	print("*****************")

	# Print sorted dictionary word & count pairs
	for word in sorted_dictionary:  # Cycles through all word (keys) in dictionary until complete
		print(f"{word:<12} {dictionary[word]}")  # Prints each word (key) with count (value)


def main():
	# Desc: Program entry point; open file, call process_line on each line.
	# 		Main() should print total length of dictionary.
	# 		When finished, call pretty_print to print dictionary in tabular format.

	my_dict = {}  # Initialize dictionary
	input_file = "gettysburg.txt"	# Toggle read file name here
	# Queries user for output file name; blank entry results in input file with "_out" appendage
	output_file = input("Enter output file name (Note: Blank will default to '[input]_out.txt'): ")
	if output_file == "":
		output_file = (str.rstrip(input_file,".txt")+"_out.txt") # Appends input file name with .txt;
	else: output_file = (str.rstrip(output_file,".txt")+".txt") # Ensures output is a .txt file

	# Open read file
	try:
		with open(input_file, 'r') as fileHandleRead:  # Open file as read
			for line in fileHandleRead:  # Cycle through lines within file
				process_line(line, my_dict)
	except FileNotFoundError as e:  # Catches error if file not in same dir as .py file
		print("File not found", str(e))

	# Call process_line function
	process_line(line, my_dict)

	# Write dictionary length message
	try:
		with open(output_file, 'w') as fileHandleWrite:  # Open file as write (overwrite prev)
			# Write total dictionary length message
			fileHandleWrite.write(f"Dictionary length: {len(my_dict)}")
	except FileNotFoundError as e:  # Catches error if file not in same dir as .py file
		print("File not found", str(e))

	# Call process_file	function
	process_file(my_dict, output_file)


	# Print total dictionary length message
	# fileHandleWrite = input("Enter file name: ")	# Request user's desired file name
	# try:
	# 	with open(fileHandleWrite, 'w') as fileHandleWrite:
	# 		write_file_name.write(f"Dictionary length: {len(my_dict)}")
	# 		pretty_print(my_dict)
	# except FileNotFoundError as e: print("File not found", str(e))

if __name__ == "__main__":
	main()
