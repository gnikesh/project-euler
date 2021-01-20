"""We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""

from itertools import permutations

def is_prime(num):
	for i in range(2, int(num ** (1/2)) + 1):
		if num % i == 0:
			return False
	return True


if __name__ == "__main__":
	largest = 0
	for i in range(1, 10):
		for per in permutations([str(i) for i in range(1, i + 1)]):
			num = int("".join(per))
			if is_prime(num):
				if num > largest:
					largest = num

	print(largest)




