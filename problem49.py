"""The arithmetic sequence, 1487, 4817, 8147, 
in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
from math import sqrt
from itertools import permutations

def is_prime(num):
	for i in range(2, int(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

def gen_prime(m):
	nm = 1000
	while nm < m:
		if is_prime(nm):
			yield nm
		nm += 1


if __name__ == "__main__":
	primes = list(gen_prime(10000))
	
	for prime in primes:
		if is_prime(prime + 3330):
			if is_prime(prime + 3330 + 3330):
				digits = list(str(prime))
				perms_list = [int("".join(i)) for i in permutations(digits)]
				if (prime + 3330) in perms_list and (prime + 3330 + 3330) in perms_list:
					print("{}{}{}".format(str(prime), str(prime + 3330), str(prime + 3330 + 3330)))

	