'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

# Increase recursion depth default of 1000 in python3
import sys
sys.setrecursionlimit(5000)


# tail recursive helper function that calculates the fibonaci of of number given number n 
def f(previous, current, n):
	if n == 1 or n == 2:
		return current
	else:
		return f(current, previous + current, n - 1)

# Function to compute nth fibonacci number
def n_fibo(n):
	if n == 0 or n == 1:
		return 1
	else:
		return f(1, 1, n)


if __name__ == "__main__":
	
	length = 1
	i = 1
	while length < 1000:
		fib = n_fibo(i)
		length = len(str(fib))
		i += 1
	
	print("Index: ", i - 1)



	

