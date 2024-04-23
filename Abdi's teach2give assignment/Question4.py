"""
Question 4: Capitalize Words 
Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string. 
Examples:  
"hi"=> returns "Hi" 
"i love programming"=> returns "I Love Programming"
"""

def capitalize_words(str):
	words = str.split()
	for index in range(len(words)):
		words[index] = words[index].capitalize()
	return' '.join(words)
str = input("Enter a string: ")
result = capitalize_words(str)
print(result)