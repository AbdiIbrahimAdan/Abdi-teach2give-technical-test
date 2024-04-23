#Question 1: FizzBuzz 
#Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
#multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
#"FizzBuzz".


#number from 1 to 100
for num in range(1, 101):
	#check whether is divisible by both 3 and 5
	if (num % 3 == 0 and num % 5 == 0):
		print("FizzBuzz")
	#check if number is divisible by 3
elif(num % 3 == 0):
	print("Fizz")
#check whether it si also divisible by 5
elif(num % == 0):
	print("Buzz")
#if not divisible by either of them print num
else:
	print(num)
	