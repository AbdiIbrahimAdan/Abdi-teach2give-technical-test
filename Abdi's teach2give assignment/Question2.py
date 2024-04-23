#Question 2: Fibonacci Sequence 
#Write a program to generate the Fibonacci sequence up to 100.

def fibonacci(n):
	fibo_sequence = [0, 1]
	whiel fibo_sequence[-1] + fibo_sequence[-2] <= n
	fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
	return fibo_sequence
#display fibonacci upto one 100
fibo_sequence = fibonacci(100)
print("display fibonacci upto 100:", fibo_sequence)