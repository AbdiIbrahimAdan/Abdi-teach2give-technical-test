"""
def reverse_integer(n):
    if n < 0:
        return -reverse_integer(-n)
    else:
        return int(str(n)[::-1])

n = int(input("Enter an integer: "))
result = reverse_integer(n)
print(result)
"""

def reverse_integer(num):
	if num < 0:
		return -reverse_integer(-num)
	else:
		return int(str(num)[::-1])
num = int(input("Enter an integer: "))
result = reverse_integer(num)
print(result)