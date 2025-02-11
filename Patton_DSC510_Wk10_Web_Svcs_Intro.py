# DSC 510
# Week 10
# Programming Assignment
# Author: John Patton
# 16 Feb 2025
# Desc: Interact w/API web service, extract JSON data, & parse the JSON response.
#
# Wk10:

def main()

# https://api.chucknorris.io/jokes/random
# https://catfact.ninja/fact
# https://uselessfacts.jsph.pl/

if __name__ == "__main__":
	main()

# Demonstrate that you can interact with a web service to extract data in JSON and then parse the JSON response. We’ve already looked at several examples of API integration from a Python perspective and this week we’re going to write a program that uses an open API to obtain data for the end user. This program will teach you the fundamentals of interacting with a free API to make a GET request, retrieve JSON data, and Parse JSON data. All of these are fundamental concepts for data science.
# Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes. By default, the API will deliver random jokes, however you should choose category dev for your category and only generate jokes of this category unless you give the user the option to select a category which is also feasible. I'll leave this up to you since it’s your program, however, defaulting to random is not acceptable.
# If you would prefer you can also use an alternative API from HTTP API for useless facts to generate a random useless fact or Cat Fact Ninja to generate a random cat fact.
# The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the relevant data.
# If you choose the Chuck Norris API you should output the “Value”.
# If you choose uselessfacts API you should output the fact’s ‘text’.
# If you choose Catfact API you should output the "fact”.
# The following Requirements are the same regardless of which API you use.
# Your program should allow the user to request a joke, useless fact, or catfact as many times as they would like. You should make sure that your program does error checking at this point including requests specific exceptions. If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about string functions you might be able to call.
# Your program must include a header as in previous weeks.
# Your program must have a properly defined main method and a properly defined call to main.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
# Your program must include a welcome message for the user.
# Your program must also have try blocks to catch HTTP Requests exceptions.
# Must have good coding practices.
# Your program must generate “pretty” output. Simply dumping a bunch of JSON data to the screen with no context doesn’t represent “pretty.” Once you extract the JSON data it should be printed for the user.