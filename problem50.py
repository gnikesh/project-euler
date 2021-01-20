"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import math

# Generate all primes less than n
def gen_prime(n):
	for i in range(2, n):
		for j in range(2, int(math.sqrt(i)) + 1):
			if i % j == 0:
				break
		else:
			yield i



if __name__ == "__main__":
	limit = 1000000

	sq_limit = int(limit ** (1/2)) + 1
	
	# Create prime generator
	primes = list(gen_prime(limit))
	# print(primes)
	print("Primes Generated")

	lseq = 0
	length = 0
	last_j = len(primes)
	largest = 0

	for i in range(len(primes)):
		for j in range(i + length, last_j):
			sol = sum(primes[i:j])
			
			if sol < limit:
				if sol in primes:
					length = j - i
					largest = sol
			else:
				last_j = j + 1
				break

	print(largest)


	
