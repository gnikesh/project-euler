# Return if given number is prime or not
def is_prime(n):
	for i in range(2, int(n ** (1/2)) + 1):
		if n % i == 0:
			return False
	return True


# Return maximum number of consecutive primes for given a and b
def get_max_prime(a, b):
	prime_count = 0
	n = 0
	while n <= prime_count:
		res = n ** 2 + a * n + b
		if res < 0:
			return 0

		if is_prime(res):
			prime_count += 1
		n += 1

	return n - 1


if __name__ == "__main__":

	max_primes, max_a, max_b = 0, 0, 0
	for a in range(-999, 1000):
		for b in range(-1000, 1001):
			t_c_prime = get_max_prime(a, b)
			if t_c_prime > max_primes:
				max_a, max_b, max_primes = a, b, t_c_prime
				
	print(max_a, max_b, max_primes)
	print("Product: ", max_a * max_b)
