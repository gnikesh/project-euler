def fact(n):
	product = 1
	for i in range(1, n + 1):
		product *= i

	return product

def main():
	for i in range(3, 1000):
		sum = 