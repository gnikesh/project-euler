"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the 
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

1387596402

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations


if __name__ == "__main__":
	primes = []
	total_sum = 0
	for i in range(2, 17+1):
		is_prime = True
		for j in range(2, int(i ** 1/2) + 1):
			if i % j == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(i)

	for number in permutations(list("0123456789")):
		number = "".join(number)
		has_property = True
		i = 1
		for prime in primes:
			if int(number[i:i+3]) % prime == 0:
				i += 1
			else:
				has_property = False
				break
		if has_property:
			total_sum += int(number)
	print(total_sum)

