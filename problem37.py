"""The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, and 
remain prime at each stage: 3797, 797, 97, and 7. Similarly we can 
work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def is_prime(num):
	if num == 1:
		return False

	for i in range(2, int(num ** (1/2)) + 1):
		if num % i == 0:
			return False

	return True


if __name__ == "__main__":
	total_primes = 0
	seen_primes = set()
	num = 10
	total_sum = 0
	while total_primes != 11:
		if not is_prime(num):
			num += 1
			continue

		s_num = str(num)
		num_length = len(s_num)
		
		t_prime = True
		
		# For left
		for i in range(num_length):
			if int(s_num[i:]) in seen_primes:
				continue

			if not is_prime(int(s_num[i:])):
				t_prime = False
				break

			seen_primes.add(int(s_num[i:]))
		
		# For right
		for i in range(num_length, 0, -1):
			if int(s_num[:i]) in seen_primes:
				continue

			if not is_prime(int(s_num[:i])):
				t_prime = False
				break

			seen_primes.add(int(s_num[:i]))

		if t_prime:
			total_sum += num
			total_primes += 1
		
		num += 1
		
		

	print("TOTAL: ", total_sum)