"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
"""
from math import sqrt

def gen_prime(m):
	p_count = 0
	num = 2
	while p_count < m:
		is_prime = True
		for i in range(2, int(sqrt(num)) + 1):
			if num % i == 0:
				is_prime = False
				break

		if is_prime:
			yield num
			p_count += 1
		
		num += 1


def prime_factor_num(num):
	prime_factors = 0
	a = set()
	i = 2
	while i < int(sqrt(num)) or num == 1:
		if num % i == 0:
			num = num // i
			a.add(i)
			i -= 1
		i += 1
	return len(a) + 1



if __name__ == "__main__":
	starting_number = 2 * 3 * 5 * 7
	stop = False
	while not stop:
		if prime_factor_num(starting_number) == 4:
			if prime_factor_num(starting_number + 1) == 4:
				if prime_factor_num(starting_number + 2) == 4:
					if prime_factor_num(starting_number + 3) == 4:
						print(starting_number)
						stop = True
		starting_number += 1






