"""Question 3: Power of Two 
Write a program that takes an integer as input and returns true if the input is a power of two. 
Examples:  
8=> returns true 
6=> returns false"""

def power_of_two(num):
	if num <= 0:
		return False
	else:
		return (num & (num - 1)) == 0
num = int(input("Enter an integer:"))
if power_of_two(num):
	print("True")
else:
	print("False")
	