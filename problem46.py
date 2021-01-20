"""It was proposed by Christian Goldbach that every odd 
composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from math import sqrt

def gen_prime(m):
	n = 2
	i = 0
	p_count = 0
	while p_count < m:
		if is_prime(n):
			yield n
			p_count += 1
		n += 1

def is_prime(num):
	for i in range(2, int(num ** 1/2) + 1):
		if num % i == 0:
			return False
	return True

if __name__ == "__main__":

	primes = list(gen_prime(10))
	
	num = 3
	while True:
		is_num = True
		for p in primes:
			if p > num:
				break

			if sqrt((num - p) / 2) == int(sqrt((num - p) / 2)):
				is_num = False
				break

		if primes[-1] < num:
			primes = list(gen_prime(len(primes) + 10))
		
		if is_num:
			print(num)
			break
		num += 2



