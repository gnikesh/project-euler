'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with 
denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

'''
My Solution:
Length of repeating decimal n, L(n) = n - 1 if and only if n is prime and 10 is primitive root modulo n.

So, the longest length of repeating digit sequence (reptend) would be 1 less than n, for the largest n
that satiesfies above condition.

Not sure if largest non-prime number less than 1000 will have repeating digit sequence that would be longer 
than that of the largest prime number less than 1000 (983 in this case).

source: https://en.wikipedia.org/wiki/Repeating_decimal

'''

from math import gcd

# Function to test if n is prime or not
def is_prime(n):
	for i in range(2, int(n ** (1/2)) + 1):
		if n % i == 0:
			return False
	return True

# Function to test if rt(10) is primitive root modulo n 
def has_primitive_root(n, rt=10):
	true_set = set([i for i in range(1, n)])
	result_set = set()

	for i in range(1, n + 1):
		result_set.add(10 ** i % n)

	if true_set == result_set:
		return True

	return False


if __name__ == "__main__":
	maximum = 0
	for i in range(1, 1000):
		if is_prime(i) and has_primitive_root(i):
			maximum = i

	print(maximum)

