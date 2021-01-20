'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

# My solution: Brute force with only 1_digit x 4_digit and 2_digit x 3_digit numbers permutations

from itertools import permutations



def is_pandigital(n: int, m: int, prod: int) -> bool:
	"""Checks if given n x m = prod is pandigital or not.
	"""
	total_numbers = set([i for i in range(1, 10)])
	numbers_got = [int(i) for i in list(str(m)) + list(str(n)) + list(str(prod))]

	if len(total_numbers) == len(numbers_got) and total_numbers == set(numbers_got):
		return True

	return False


if __name__ == "__main__":

	# Store previously seen products
	pandigitals = []
	numbers = [i for i in range(1, 10)]
	

	# Possible permutations that could have total of 9 digits with multiplicand, multiplier and product are:
	# 1_digit x 4_digit numbers or vice versa
	# 2_digit x 3_digit numbers or vice versa
	# since we just need unique product, 1_digit x 4_digit and 4_digit x 1_digit are equivalent
	# If we take a number as multiplicand, it cannot be in multiplier which further reduces our search space

	# 1_digit x 4_digit = product
	for n in permutations(numbers, 1):
		for m in permutations([i for i in numbers if n[0] != i], 4):
			n_num = int("".join(map(str, n)))
			m_num = int("".join(map(str, m)))
			product = n_num * m_num
			if not product in pandigitals:
				if is_pandigital(n_num, m_num, product):
					pandigitals.append(product)
	
	# 2_digit x 3_digit = product
	for n in permutations(numbers, 2):
		for m in permutations([i for i in numbers if n[0] != i], 3):
			n_num = int("".join(map(str, n)))
			m_num = int("".join(map(str, m)))
			product = n_num * m_num
			if not product in pandigitals:
				if is_pandigital(n_num, m_num, product):
					pandigitals.append(product)
	

	print("Sum: {}".format(sum(pandigitals)))


