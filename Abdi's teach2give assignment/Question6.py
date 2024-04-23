"""
Question 6: Count Vowels 
Write a program that counts the number of vowels in a sentence. 
eg " Hello World " => returns 2

"""

def count_vowels(str):
	vowels = "aeiouAEIOU"
	count = 0
	for char in str:
		if char in vowels:
			count += 1
	return count
str = input("Enter a sentence: ")
result = count_vowels(str)
print("Number of vowels:", result)
